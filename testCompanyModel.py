import os
from datetime import datetime as date
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

print(f"Today's date and time:\
 {date.today().year}-{date.today().month}-{date.today().day}_{date.today().hour}:{date.today().minute}:{date.today().second}\n")

cur_ticker = input('Enter the NASDAQ/NYSE ticker of your company (ex. for Coca-Cola: KO): ').upper()
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
	print(' - '+c)

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
				print(f"\nThere are {copy_amt} models with the parameters you've entered in the ./models folder.")
				copy_no = int(input("Please enter the number of the copy you'd like to select: "))
				if copy_no > copy_amt or copy_no <= 0:
					print(f"That number is out of range.\n")
				else:
					valid_copy = True
			except:
				print('Invalid input.')
	
	model_name = f'LSTM_{cur_ticker}_seq:{seq_length}_target:{target_length}_ind:{ind_string}_copy:{copy_no}.model'
	print(f'\nModel found: {model_name}\n')
	print(f'cur_ticker = {cur_ticker}')
	print(f'seq_length = {seq_length}')
	print(f'target_length = {target_length}')
	print(f'indicator_arr = {indicator_arr}')
	print(f'copy_no = {copy_no}\n')

	stock_data, cur_ticker, indicator_arr = get_stock_stats(cur_ticker, target_length, indicator_arr)
	get_stock_visual(stock_data, cur_ticker, indicator_arr)

	testing_data = sort_data(stock_data, target_length)
	x_test, y_test = preprocess_stock_data(testing_data, seq_length)

	model = load_model(f'./models/{model_name}')
	print('\nProcessing...')
	model.evaluate(x_test, y_test)
	print('')
else:
	print('\nNo model found for those parameters. Please restart this file and try again.\n')