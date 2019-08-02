import numpy as np
from datetime import datetime as date
from getStockStats import get_stock_stats, evaluate_price, get_stock_visual
from makeStockRNN import sort_stock_data, preprocess_stock_data, make_stock_rnn
import os

print(f"Today's date and time:\
 {date.today().year}-{date.today().month}-{date.today().day}_{date.today().hour}:{date.today().minute}:{date.today().second}\n")

cur_ticker = input('Enter the NASDAQ/NYSE ticker of your company (ex. for Coca-Cola: KO): ').upper()
print('')

print('\nEach prediction uses the last <seq_length> days of information containing each indicator from the <indicator_arr> list\
 all as reference data to predict whether the price will rise or fall in <target_length> days.\n')

not_num1 = True
while not_num1 == True:
	try:
		seq_length = int(input('Enter your desired seq_length: '))
		not_num1 = False
	except:
		print('That is an invalid input.\n')


not_num2 = True
while not_num2 == True:
	try:
		target_length = int(input('Enter your desired target_length: '))
		not_num2 = False
	except:
		print('That is an invalid input.\n')

print('')

indicator_arr = []
is_complete = False
i = 1

while is_complete == False:
	cur_ind = input(f'Enter the name of indicator #{i} (ex. close_26_ema): ')
	indicator_arr.append(cur_ind)
	print('\n---------------------------')
	print('Current list of indicators:')
	for c in indicator_arr:
		print(' - '+c)
	print('---------------------------')
	is_finished = input('\nIs this list complete? (y/n): ')
	print('')
	if is_finished.upper() == 'Y':
		is_complete = True
	i += 1

print('\n-----------------------------')
print('Tentative list of indicators:')

for c in indicator_arr:
	print(c)

print('-----------------------------')

stock_data, cur_ticker, indicator_arr = get_stock_stats(cur_ticker, target_length, indicator_arr)

print('\n-----------------------------------------------------------')
print('Final list of indicators (invalid indicators were removed):')

for c in indicator_arr:
	print(c)

print('-----------------------------------------------------------')

training_data, testing_data = sort_stock_data(stock_data, target_length)
get_stock_visual(stock_data, cur_ticker, indicator_arr)

x_train, y_train = preprocess_stock_data(training_data, seq_length)
x_test, y_test = preprocess_stock_data(testing_data, seq_length)

print(f'Train data: {len(x_train)}. Test data: {len(x_test)}.')
print(f'Train sells: {y_train.count(0)}. Buys: {y_train.count(1)}.')
print(f'Test sells: {y_test.count(0)}. Buys: {y_test.count(1)}.\n')

not_num3 = True
while not_num3 == True:
	try:
		EPOCHS = int(input('Enter your desired amount of epochs: '))
		not_num3 = False
	except:
		print('That is an invalid input.\n')

print('')

file = open('./current_text.txt', 'w')
for cur_ind in indicator_arr:
	file.write(cur_ind+' ')
file.close()

file = open('./current_text.txt', 'r')
ind_string = file.read()[:-1]
file.close()

file = open('./current_text.txt', 'w')
file.close()

copy_no = 1
for cur_file in os.listdir('./models'):
	if cur_ticker in cur_file:
		if str(seq_length) in cur_file:
			if str(target_length) in cur_file:
				if ind_string in cur_file:
					copy_no += 1

make_stock_rnn(x_train, y_train, x_test, y_test, seq_length, target_length, cur_ticker, ind_string, copy_no, EPOCHS)