import tensorflow as tf
from tensorflow.keras.models import load_model
from datetime import datetime as date
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price
from makeStockRNN import sort_stock_data, preprocess_stock_data

tickers = ['AAPL', 'AMZN', 'F', 'FB', 'GOOGL', 'KO', 'MSFT', 'NFLX', 'NVDA','TSLA', 'UPS']

eval_dict = {
	0 : 'Bad',
	1 : 'Good',
	None : 'Neutral'
}

ticker_dict = {
	'AAPL' : 'Apple',
	'AMZN' : 'Amazon',
	'F' : 'Ford',
	'FB' : 'Facebook',
	'GOOGL' : 'Google',
	'KO' : 'Coca-Cola',
	'MSFT' : 'Microsoft',
	'NFLX' : 'Netflix',
	'NVDA' : 'Nvidia',
	'TSLA' : 'Tesla',
	'UPS' : 'United Parcel Service',
}

print(f"Today's date and time: {date.today().year}-{date.today().month}-{date.today().day}_{date.today().hour}:{date.today().minute}:{date.today().second}\n")
print('COMPANIES')
print('0 : AAPL (Apple)')
print('1 : AMZN (Amazon)')
print('2 : F (Ford)')
print('3 : FB (Facebook)')
print('4 : GOOGL (Google)')
print('5 : KO (Coca-Cola)')
print('6 : MSFT (Microsoft)')
print('7 : NFLX (Netflix)')
print('8 : NVDA (Nvidia)')
print('9 : TSLA (Tesla)')
print('10 : UPS (United Parcel Service)\n')

val = int(input('Enter the integer of the corresponding company: '))

stock_data = get_stock_stats(tickers[val], 30)
get_stock_visual(stock_data, ticker_dict.get(tickers[val]))

train_data, test_data = sort_stock_data(stock_data, 30)

x_test, y_test = preprocess_stock_data(test_data, 60)

model = load_model(f'best_models/RNN_{ticker_dict.get(tickers[val])}.model')
model.evaluate(x_test, y_test)
