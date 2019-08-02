import tensorflow as tf
from tensorflow.keras.models import load_model
from getStockStats import get_stock_stats, get_stock_visual, evaluate_price
from makeStockRNN import preprocess_stock_data
import os

def sort_data(df, target_length):
	df = df[:-target_length]

	time_stamps = sorted(df.index.values)
	last_five_pct = time_stamps[-int(0.05*len(df.index))]

	testing_data = df[(last_five_pct <= df.index)]

	print(f'\n\nDone! (sort_stock_data)')
	return testing_data

cur_ticker = input('Enter the NASDAQ/NYSE ticker of your company (ex. for Coca-Cola: KO): ').upper()

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
q = 1

while is_complete == False:
	cur_ind = input(f'Enter the name of indicator #{q} (ex. close_26_ema): ')
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
	q += 1

print('\n-----------------------------')
print('List of indicators:')

for c in indicator_arr:
	print(c)

print('-----------------------------')

file = open('./current_text.txt', 'w')
for cur_ind in indicator_arr:
	file.write(cur_ind+' ')
file.close()

file = open('./current_text.txt', 'r')
ind_string = file.read()[:-1]
file.close()

file = open('./current_text.txt', 'w')
file.close()

copy_amt = 0
for cur_file in os.listdir('./models'):
	if cur_ticker in cur_file:
		if str(seq_length) in cur_file:
			if str(target_length) in cur_file:
				if ind_string in cur_file:
					copy_amt += 1

if copy_amt > 0:
	copy_no = 1
	if copy_amt == 1:
		pass
	else:
		valid_copy = False
		while valid_copy == False:
			try:
				copy_no = int(input(f"There are {copy_amt} models with the same parameters in the ./models folder. Please enter the number of the copy you'd like to select: "))
				if copy_no > copy_amt or copy_no <= 0:
					print(f"That number is out of range.\n")
				else:
					valid_copy = True
			except:
				print('Invalid input.\n')
	
	print(f'\ncur_ticker = {cur_ticker}')
	print(f'seq_length = {seq_length}')
	print(f'target_length = {target_length}')
	print(f'indicator_arr = {indicator_arr}\n')

	stock_data, cur_ticker, indicator_arr = get_stock_stats(cur_ticker, target_length, indicator_arr)
	get_stock_visual(stock_data, cur_ticker, indicator_arr)

	testing_data = sort_data(stock_data, target_length)
	x_test, y_test = preprocess_stock_data(testing_data, seq_length)

	model = load_model(f'./models/LSTM_{cur_ticker}_seq:{seq_length}_target:{target_length}_ind:{ind_string}_copy:{copy_no}.model')
	print('\nProcessing...')
	model.evaluate(x_test, y_test)
else:
	print(f'No model found for those parameters. Please restart this file and try again.')