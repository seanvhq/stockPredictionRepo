import csv
from datetime import datetime as date
from getStockStats import get_stock_stats, evaluate_price, get_stock_visual
from makeStockRNN import sort_stock_data, preprocess_stock_data, make_stock_rnn
	
print(f"Today's date and time:\
 {date.today().year}-{date.today().month}-{date.today().day}_{date.today().hour}:{date.today().minute}:{date.today().second}\n")

cur_ticker = input('Enter the NASDAQ ticker of your company (ex. KO): ').upper()
company_name = input('Enter the name of your company (ex. Coca-Cola): ')
print(f'\nYou chose: {cur_ticker} ({company_name})\n')

print('\nEach prediction uses the last <seq_length> days of information as reference data\
 to predict whether the price will rise or fall in <target_length> days.\n')

seq_length = int(input('Enter your desired seq_length: '))
target_length = int(input('Enter your desired target_length: '))

stock_data = get_stock_stats(cur_ticker, target_length)
training_data, testing_data = sort_stock_data(stock_data, target_length)
get_stock_visual(stock_data, company_name)

x_train, y_train = preprocess_stock_data(training_data, seq_length)
x_test, y_test = preprocess_stock_data(testing_data, seq_length)

print(f'Train data: {len(x_train)}. Test data: {len(x_test)}.')
print(f'Train sells: {y_train.count(0)}. Buys: {y_train.count(1)}.')
print(f'Test sells: {y_test.count(0)}. Buys: {y_test.count(1)}.\n')

EPOCHS = int(input('Enter amount of desired epochs: '))
print('')

make_stock_rnn(x_train, y_train, x_test, y_test, seq_length, target_length, company_name, EPOCHS)

file = open('company_lengths.csv', 'a')
writer = csv.writer(file)
writer.writerow([company_name,seq_length,target_length])
file.close()
