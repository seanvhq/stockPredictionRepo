import numpy as np
import pandas as pd
import tensorflow as tf
from collections import deque
from sklearn import preprocessing
from tensorflow.keras.models import load_model
from datetime import datetime as date
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price

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

	return np.array(X)

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

action_dict = {
	0 : 'sell',
	1 : 'buy',
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

x = preprocess_data(stock_data, 60)

model = load_model(f'best_models/RNN_{ticker_dict.get(tickers[val])}.model')
print('\nProcessing...')
predictions = model.predict([x])
print(f'\n\nGiven the last 2 months of data, chances are that you should {action_dict.get(np.argmax(predictions[-1]))}.\n')
