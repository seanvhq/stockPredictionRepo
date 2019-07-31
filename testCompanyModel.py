import csv
import tensorflow as tf
from tensorflow.keras.models import load_model
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price
from makeStockRNN import preprocess_stock_data

def sort_data(df, target_length):
	df = df[:-target_length]

	time_stamps = sorted(df.index.values)
	last_five_pct = time_stamps[-int(0.05*len(df.index))]

	testing_data = df[(last_five_pct <= df.index)]

	print(f'\n\nDone! (sort_stock_data)')
	return testing_data

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
x_test, y_test = preprocess_stock_data(testing_data, seq_length)

model = load_model(f'./models/LSTM_{cur_ticker}.model')
print('\nProcessing...')
model.evaluate(x_test, y_test)