import time
from textblob import TextBlob
from selenium import webdriver

def current_companies_sentiments(companies):
	eval_ints = []

	eval_dict = {
		0 : 'Bad',
		1 : 'Good',
		None : 'Neutral'
	}

	site = 'https://finance.yahoo.com'
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
	
	for company_name in companies:
		cur_eval = 0
		k = 1
		print(f'\nCurrent company: {company_name}')
		for elem in link_elems:
			if 'finance.yahoo' in elem.get_attribute('href'):
				if company_name in elem.text:
					print(f'Article #{k} name: ' + elem.text)
					driver2 = webdriver.Firefox(executable_path='./geckodriver')
					driver2.get(elem.get_attribute('href'))

					try:
						driver2.find_element_by_xpath('//button[@name="agree"]').click()
					except:
						pass

					print(f'Yahoo Finance {company_name} article #{k} opened.')
					article_text = driver2.find_elements_by_xpath('//article/div/p')
					file = open('./current_text.txt', 'w')

					for p in article_text:
						if p.get_attribute('content')[:7] == '<a href':
							break
						file.write(p.text+' ')

					file.close()
					file = open('./current_text.txt', 'r')

					polarity = TextBlob(file.read()).sentiment.polarity

					if polarity < 0:
						eval_int = 0
						cur_eval -= 1
					elif polarity > 0:
						eval_int = 1
						cur_eval += 1
					else:
						eval_int = None

					print(f'{company_name} article #{k} sentiment: {eval_dict.get(eval_int)}.\n')
					k += 1

					file.close()
					file = open('./current_text.txt', 'w')
					file.close()
					driver2.close()

		if cur_eval > 0:
			overall_eval_int = 1
		elif cur_eval < 0:
			overall_eval_int = 0
		else:
			overall_eval_int = None

		print(f'Current {company_name} sentiment: {eval_dict.get(overall_eval_int)}.')

		if overall_eval_int == None:
			overall_eval_int = 0
		
		eval_ints.append([company_name, overall_eval_int])

	driver.close()

	print(f'\n\nDone! (current_companies_sentiments({companies}))')
	return eval_ints
