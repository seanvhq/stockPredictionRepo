from pandas_datareader import data as wb
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import numpy as np
import pandas as pd

from stockstats import StockDataFrame as sdf
from matplotlib import pyplot as plt
from pylab import rcParams

def evaluate_price(f, c):
    if f > c:
        return 1
    else:
        return 0

def get_stock_stats(cur_ticker, target_length, indicator_arr):
	print('')
	inds_to_remove = []
	is_stocks = False
	while is_stocks == False:
		try:
			stock_data = wb.DataReader(cur_ticker, data_source='yahoo', start='1900-1-1')
			is_stocks = True
		except:
			cur_ticker = input('Invalid NASDAQ/NYSE ticker. Try inputting the ticker again: ').upper()

	indicators = sdf.retype(stock_data)

	for cur_ind in indicator_arr:
		try:
			indicators[cur_ind]
		except:
			inds_to_remove.append(cur_ind)

	print('')

	for remove_ind in inds_to_remove:
		print(f'Invalid indicator removed: {remove_ind}')
		indicator_arr.remove(remove_ind)

	stock_data['future'] = stock_data['close'].shift(-target_length)
	stock_data['eval'] = list(map(evaluate_price, stock_data['future'], stock_data['close']))
	del stock_data['future']

	print(f'\n\nDone! (get_stock_stats({cur_ticker}, {target_length}, {indicator_arr}))')
	return stock_data, cur_ticker, indicator_arr

def get_stock_visual(stock_data, cur_ticker, indicator_arr):
	rcParams['figure.figsize'] = 15, 7
	plt.plot(stock_data['open'], label='Open')
	plt.plot(stock_data['close'], label='Close')
	plt.title(cur_ticker+' Stock Data')
	plt.legend()
	plt.show()
	
	for cur_ind in indicator_arr:
		rcParams['figure.figsize'] = 15, 7
		plt.plot(stock_data[cur_ind])
		plt.title(cur_ticker+' '+cur_ind)
		plt.show()

	print('\n\nDone! (get_stock_visual)')
