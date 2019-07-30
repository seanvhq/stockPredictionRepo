import csv
from datetime import datetime as date
from currentCompanySentiment import current_company_sentiment

companies = []
is_complete = False
i = 1

while is_complete == False:
	cur_company = input(f'Enter the name of company #{i} (ex. Coca-Cola): ')
	companies.append(cur_company)
	print('\nCurrent list of companies:')
	for c in companies:
		print(c)
	is_finished = input('\nIs this list complete? (y/n): ')
	print('')
	if is_finished.upper() == 'Y':
		is_complete = True
	i += 1

print('\nFinal list of companies:')

for c in companies:
	print(c)

print('')

for company_name in companies:
	overall_eval_int = current_company_sentiment(company_name)

	file = open(f'./sentiments/{company_name}_sentiments.csv', 'a')
	writer = csv.writer(file)
	writer.writerow([f'{date.today()}', overall_eval_int])
	file.close()
