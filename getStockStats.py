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

def get_stock_stats(cur_ticker, target_length):
	stock_data = wb.DataReader(cur_ticker, data_source='yahoo', start='1900-1-1')
	indicators = sdf.retype(stock_data)
	indicators['volume_delta']
	indicators['boll_ub']
	indicators['boll_lb']
	indicators['macd']
	indicators['open_2_sma']
	stock_data['future'] = stock_data['close'].shift(-target_length)
	stock_data['eval'] = list(map(evaluate_price, stock_data['future'], stock_data['close']))
	del stock_data['future']

	return stock_data

def get_stock_visual(stock_data, company_name):
	rcParams['figure.figsize'] = 15, 7
	plt.plot(stock_data['close'], label='Close Price')
	plt.plot(stock_data['boll_ub'], label='BB Upper Band')
	plt.plot(stock_data['boll_lb'], label='BB Lower Band')
	plt.plot(stock_data['close_26_ema'], label='26-Day EMA (Close Price)')
	plt.title(company_name+' Stock Data')
	plt.legend()
	plt.show()

	rcParams['figure.figsize'] = 15, 7
	plt.plot(stock_data['macd'], label='MACD')
	plt.plot(stock_data['macds'], label='MACD Signal Line')
	plt.plot(stock_data['macdh'], label='MACD Histogram')
	plt.title(company_name+' MACD Data')
	plt.legend()
	plt.show()

	rcParams['figure.figsize'] = 15, 7
	plt.plot(stock_data['volume_delta'], label='Volume Delta Against Previous Day')
	plt.title(company_name+' Volume Delta')
	plt.show()

	print('\n\nDone! (get_stock_visual)')
