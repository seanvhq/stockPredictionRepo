import csv
from datetime import datetime as date
from currentCompaniesSentiments import current_companies_sentiments

companies = []
is_complete = False
i = 1

while is_complete == False:
	cur_company = input(f'Enter the name of company #{i} (ex. Coca-Cola): ')
	companies.append(cur_company)
	print('\n--------------------------')
	print('Current list of companies:')
	for c in companies:
		print(' - '+c)
	print('--------------------------')
	is_finished = input('\nIs this list complete? (y/n): ')
	print('')
	if is_finished.upper() == 'Y':
		is_complete = True
	i += 1

print('\n------------------------')
print('Final list of companies:')

for c in companies:
	print(c)

print('------------------------')
print('')

eval_ints = current_companies_sentiments(companies)

for company_name, overall_eval_int in eval_ints:
	csv_file = open(f'./sentiments/{company_name}_sentiments.csv', 'a')
	writer = csv.writer(csv_file)
	writer.writerow([date.today(), overall_eval_int])
	csv_file.close()
