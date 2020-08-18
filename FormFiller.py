from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = str(input("Insert chromedriver directory: "))
browser = webdriver.Chrome(chromedriver)
browser.get("https://dev-1.clicktrans.pl/register-test/courier")

class OrderForm:
	@staticmethod
	def FillForm():
		arrone = ["user_register_company_name", "user_register_email", "user_register_name", "user_register_phone", "user_register_plainPassword", "sel-agreement-regulations-label", "sel-agreement-personal-label", "user_register_submit"]
		arrtwo = ["KOWALSKI SA", "jankowalski@gmail.com", "JAN KOWALSKI", "777777777", "jan7kowalski"]
		length = len(arrone)
		for i in range(length):
			if i <= 4:
			    browser.find_element_by_id(arrone[i]).send_keys(arrtwo[i])
			elif i >= 5:
			    browser.find_element_by_id(arrone[i]).click()
		OrderForm.CheckFormMessage('OK - some registration logic is mocked')
		#browser.close()
		#browser.quit()
	
	@staticmethod
	def CheckFormMessage(message):
		if message in browser.page_source:
			print ('Form was sent correctly.')
		else:
			print ('Form was not sent correctly. Check data.')
	

OrderForm.FillForm()