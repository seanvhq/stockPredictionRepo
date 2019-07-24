import time

from textblob import TextBlob
from selenium import webdriver
from datetime import datetime as date

def current_company_sentiment():
	cur_eval = 0

	eval_dict = {
		0 : 'Bad',
		1 : 'Good',
		None : 'Neutral'
	}

	k = 1
	site = 'https://finance.yahoo.com'
	tickers = ['AAPL', 'AMZN', 'F', 'FB', 'GOOGL', 'KO', 'MSFT', 'NFLX', 'NVDA','TSLA', 'UPS']

	ticker_dict = {
		'AAPL' : 'Apple',
		'AMZN' : 'Amazon',
		'F' : 'Ford',
		'FB' : 'Facebook',
		'GOOGL' : 'Google',
		'KO' : 'Coca-Cola',
		'MSFT' : 'Microsoft',
		'NFLX' : 'Netflix',
		'NVDA' : 'Nvidia',
		'TSLA' : 'Tesla',
		'UPS' : 'United Parcel Service',
	}
	
	print(f"Today's date and time: {date.today()}\n")
	print('COMPANIES')
	print('0 : AAPL (Apple)')
	print('1 : AMZN (Amazon)')
	print('2 : F (Ford)')
	print('3 : FB (Facebook)')
	print('4 : GOOGL (Google)')
	print('5 : KO (Coca-Cola)')
	print('6 : MSFT (Microsoft)')
	print('7 : NFLX (Netflix)')
	print('8 : NVDA (Nvidia)')
	print('9 : TSLA (Tesla)')
	print('10 : UPS (United Parcel Service)\n')
	val = int(float(input('Get the most recent sentiment on a specific company. Enter an integer: ')))

	cur_ticker = tickers[val]
	company_name = ticker_dict.get(cur_ticker)
	print('\nYou chose:\n{0} : {1} ({2})\n'.format(str(val), cur_ticker, company_name))
	driver = webdriver.Firefox(executable_path='./geckodriver')
	driver.get(site)

	try:
		driver.find_element_by_xpath('//button[@name="agree"]').click()
	except:
		pass

	for scroll in range(20):
		driver.execute_script('window.scrollBy(0, 2000)')
		time.sleep(2)

	link_elems = driver.find_elements_by_xpath('//ul/li/div/div/div/h3/a')

	for elem in link_elems:
		if 'finance.yahoo' in elem.get_attribute('href'):
			if (company_name.upper() in elem.text.upper()) or (cur_ticker.upper() in elem.text.upper()):
				print('Article #{0} name: '.format(str(k)) + elem.text)
				driver2 = webdriver.Firefox(executable_path='./geckodriver')
				driver2.get(elem.get_attribute('href'))

				try:
					driver2.find_element_by_xpath('//button[@name="agree"]').click()
				except:
					pass

				print('Yahoo Finance {0} article #{1} opened.'.format(company_name, k))
				article_text = driver2.find_elements_by_xpath('//article/div/p')
				file = open('current_text.txt', 'w')

				for p in article_text:
					if p.get_attribute('content')[:7] == '<a href':
						break
					file.write(p.text+' ')

				file.close()
				file = open('current_text.txt', 'r')

				polarity = TextBlob(file.read()).sentiment.polarity

				if polarity < 0:
					eval_int = 0
					cur_eval -= 1
				elif polarity > 0:
					eval_int = 1
					cur_eval += 1
				else:
					eval_int = None

				print('{0} article #{1} sentiment: {2}.\n'.format(company_name, str(k), eval_dict.get(eval_int)))
				k += 1

				file.close()
				driver2.close()

	driver.close()
	file = open('current_text.txt', 'w')
	file.close()
		    
	if cur_eval > 0:
		overall_eval_int = 1
	else:
		overall_eval_int = 0

	print('Current {0} sentiment: {1}.'.format(company_name, eval_dict.get(overall_eval_int)))

	print(f'\n\nDone! (current_company_sentiment({val}))')

	return cur_ticker, company_name, overall_eval_int
