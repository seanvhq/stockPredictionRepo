import random
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from tensorflow.keras.layers import Dropout, Dense, BatchNormalization, LSTM
from sklearn import preprocessing
from collections import deque
from datetime import datetime as date

def sort_stock_data(df, target_length):
	df = df[:-target_length]

	time_stamps = sorted(df.index.values)
	last_five_pct = time_stamps[-int(0.05*len(df.index))]

	training_data = df[(df.index < last_five_pct)]
	testing_data = df[(last_five_pct <= df.index)]

	print(f'\n\nDone! (sort_stock_data)')
	return training_data, testing_data

def preprocess_stock_data(dataframe, seq_length):
	buys = []
	df = pd.DataFrame(dataframe)
	sells = []
	seq_data = []
	X = []
	y = []

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
			seq_data.append([np.array(prev_days), i[-1]])
    
	for seq, eva in seq_data:
		if eva == 0:
			sells.append([seq, eva])
		elif eva == 1:
			buys.append([seq, eva])
            
	limit = min(len(sells), len(buys))
	buys = buys[:limit]
	sells = sells[:limit]
    
	seq_data = sells + buys
	random.shuffle(seq_data)
    
	for seq, eva in seq_data:
		X.append(seq)
		y.append(eva)

	print('\n\nDone! (preprocess_stock_data)')
	return np.array(X), y

def make_stock_rnn(x_train, y_train, x_test, y_test, seq_length, target_length, company_name, EPOCHS):
	model = Sequential()
	model.add(LSTM(128, activation='relu', input_shape=(x_train.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())

	model.add(LSTM(128, activation='relu', input_shape=(x_train.shape[1:]), return_sequences=True))
	model.add(Dropout(0.1))
	model.add(BatchNormalization())

	model.add(LSTM(128, activation='relu', input_shape=(x_train.shape[1:])))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())

	model.add(Dense(32, activation='relu'))
	model.add(Dropout(0.2))

	model.add(Dense(2, activation='softmax'))

	opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)
	model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

	tensorboard = TensorBoard(log_dir=f'logs/{company_name}_{date.today()}')
	checkpoint = ModelCheckpoint\
    (f'./models/LSTM_{company_name}.model', monitor='val_acc', verbose=1, save_best_only=True, mode='max')

	history = model.fit\
    (x_train, y_train, batch_size=64, epochs=EPOCHS, validation_data=(x_test,y_test), callbacks=[tensorboard, checkpoint])
    
	print('\n\nDone! (make_stock_rnn)')
