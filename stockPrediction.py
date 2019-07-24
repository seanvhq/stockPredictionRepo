import csv
from datetime import datetime as date

from currentCompanySentiment import current_company_sentiment
from getStockStats import get_stock_stats, evaluate_price, get_stock_visual
from makeStockRNN import sort_stock_data, preprocess_stock_data, make_stock_rnn

#1-----
cur_ticker, company_name, overall_eval_int = current_company_sentiment()

file = open(f'{company_name}_sentiments.csv', 'a')
writer = csv.writer(file)
writer.writerow([f'{date.today()}', overall_eval_int])
file.close()
#1-----

seq_length = int(input('Enter training period (in days): '))
target_length = int(input('Enter no. of days ahead you want to look at: '))

#2-----
stock_data = get_stock_stats(cur_ticker, target_length)
training_data, testing_data = sort_stock_data(stock_data)
get_stock_visual(stock_data, company_name)
#2-----

#3-----
x_train, y_train = preprocess_stock_data(training_data, seq_length)
x_test, y_test = preprocess_stock_data(testing_data, seq_length)

print(f'Train data: {len(x_train)}. Test data: {len(x_test)}.')
print(f'Train sells: {y_train.count(0)}. Buys: {y_train.count(1)}.')
print(f'Test sells: {y_test.count(0)}. Buys: {y_test.count(1)}.\n')

make_stock_rnn(x_train, y_train, x_test, y_test, seq_length, target_length, company_name)
#3-----
