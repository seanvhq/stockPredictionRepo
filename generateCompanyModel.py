from getStockStats import get_stock_stats, evaluate_price, get_stock_visual
from makeStockRNN import sort_stock_data, preprocess_stock_data, make_stock_rnn
	
print(f"Today's date and time: {date.today().year}-{date.today().month}-{date.today().day}_{date.today().hour}:{date.today().minute}:{date.today().second}\n")

cur_ticker = input('Enter the NASDAQ ticker of your company (ex. KO): ')
company_name = input('Enter the name of your company (ex. Coca-Cola): ')
print(f'\nYou chose: {cur_ticker} ({company_name})\n')

seq_length = 60
target_length = 30

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