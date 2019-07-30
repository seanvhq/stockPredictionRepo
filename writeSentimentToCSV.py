import csv
from datetime import datetime as date
from currentCompanySentiment import current_company_sentiment

company_name, overall_eval_int = current_company_sentiment()

file = open(f'sentiments/{company_name}_sentiments.csv', 'a')
writer = csv.writer(file)
writer.writerow([f'{date.today()}', overall_eval_int])
file.close()
