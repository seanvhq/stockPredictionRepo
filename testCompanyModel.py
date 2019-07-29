import tensorflow as tf
from tensorflow.keras.models import load_model
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price
from makeStockRNN import preprocess_stock_data

def sort_data(df, target_length):
	df = df[:-target_length]

	time_stamps = sorted(df.index.values)
	last_five_pct = time_stamps[-int(0.05*len(df.index))]

	testing_data = df[(last_five_pct <= df.index)]

	return testing_data
	print(f'\n\nDone! (sort_stock_data)')

cur_ticker = input('Enter the NASDAQ ticker of your company (ex. KO): ')
company_name = input('Enter the name of your company (ex. Coca-Cola): ')
print(f'\nYou chose: {cur_ticker} ({company_name})\n')

seq_length = 60
target_length = 30

stock_data = get_stock_stats(cur_ticker, target_length)
get_stock_visual(stock_data, company_name)

testing_data = sort_data(stock_data, target_length)

x_test, y_test = preprocess_stock_data(testing_data, seq_length)

model = load_model(f'best_models/RNN_{company_name}.model')
model.evaluate(x_test, y_test)
