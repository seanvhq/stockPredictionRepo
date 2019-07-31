import numpy as np
import pandas as pd
import tensorflow as tf
from collections import deque
from sklearn import preprocessing
from tensorflow.keras.models import load_model
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price
import csv

def sort_data(df, target_length):
	df = df[:-target_length]

	time_stamps = sorted(df.index.values)
	last_five_pct = time_stamps[-int(0.05*len(df.index))]

	testing_data = df[(last_five_pct <= df.index)]

	print(f'\n\nDone! (sort_data)')
	return testing_data

def preprocess_data(dataframe, seq_length):
	df = pd.DataFrame(dataframe)
	X = []

	for col in df.columns:
		if col != 'eval':
			df[col] = df[col].pct_change()
			df = df.replace([np.inf, -np.inf], np.nan)
			df.dropna(inplace=True)
			df[col] = preprocessing.scale(df[col].values)
    
	df.dropna(inplace=True)
	prev_days = deque(maxlen=seq_length)
    
	for i in df.values:
		prev_days.append([n for n in i[:-1]])
		if len(prev_days) == seq_length:
			X.append(np.array(prev_days))

	print('\n\nDone! (preprocess_data)')
	return np.array(X)

action_dict = {
	0 : 'fall',
	1 : 'rise'
}

cur_ticker = input('Enter the NASDAQ/NYSE ticker of your company (ex. for Coca-Cola: KO): ').upper()

csv_file = open('./company_parameters.csv', 'r')
reader = csv.reader(csv_file)

for row in reader:
	if cur_ticker == row[0]:
		company_name = row[1]
		seq_length = int(row[2])
		target_length = int(row[3])
		indicator_arr = row[4].split(' ')
		break
		
csv_file.close()

print(f'\ncompany_name = {company_name}')
print(f'cur_ticker = {cur_ticker}')
print(f'seq_length = {seq_length}')
print(f'target_length = {target_length}')
print(f'indicator_arr = {indicator_arr}\n')

stock_data, cur_ticker, indicator_arr = get_stock_stats(cur_ticker, target_length, indicator_arr)
get_stock_visual(stock_data, company_name, indicator_arr)

testing_data = sort_data(stock_data, target_length)
x = preprocess_data(testing_data, seq_length)

model = load_model(f'./models/LSTM_{cur_ticker}.model')
print('\nProcessing...')
predictions = model.predict([x])
print(f'\n\nGiven the last {seq_length} days of data, chances are that, in {target_length} days,\
 the stock price will {action_dict.get(np.argmax(predictions[-1]))}.\n')