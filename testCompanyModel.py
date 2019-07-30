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

company_name = input('Enter the name of your company (ex. Coca-Cola): ')
cur_ticker = input('Enter the NASDAQ ticker of your company (ex. KO): ').upper()
print(f'\nYou chose: {cur_ticker} ({company_name})\n')

file = open('./company_lengths.csv', 'r')
reader = csv.reader(file)

for row in reader:
	if company_name == row[0]:
		seq_length = int(row[1])
		target_length = int(row[2])
		break
		
file.close()

print(f'\nCompany: {company_name}')
print(f'seq_length = {seq_length}')
print(f'target_length = {target_length}\n')

stock_data = get_stock_stats(cur_ticker, target_length)
get_stock_visual(stock_data, company_name)

testing_data = sort_data(stock_data, target_length)
x_test, y_test = preprocess_stock_data(testing_data, seq_length)

model = load_model(f'./models/LSTM_{company_name}.model')
print('\nProcessing...')
model.evaluate(x_test, y_test)
