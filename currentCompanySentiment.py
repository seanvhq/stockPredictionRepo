import time
from textblob import TextBlob
from selenium import webdriver

def current_company_sentiment(val):
	cur_eval = 0

	eval_dict = {
		0 : 'Bad',
		1 : 'Good',
		None : 'Neutral'
	}

	k = 1
	site = 'https://finance.yahoo.com'
	tickers = ['AAPL', 'AMZN', 'F', 'GOOGL', 'MSFT', 'NFLX', 'TSLA']

	ticker_dict = {
		'AAPL' : 'Apple',
		'AMZN' : 'Amazon',
		'F' : 'Ford',
		'GOOGL' : 'Google',
		'MSFT' : 'Microsoft',
		'NFLX' : 'Netflix',
		'TSLA' : 'Tesla'
	}

	cur_ticker = tickers[val]
	company_name = ticker_dict.get(cur_ticker)
	print('You chose:\n{0} : {1} ({2})\n'.format(str(val), cur_ticker, company_name))
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
			if company_name.upper() in elem.text.upper():
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

	return cur_ticker, company_name, overall_eval_int
