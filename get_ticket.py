from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
chromedriver = "D:\\downloads\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)


driver.get('https://tixcraft.com')
driver.set_window_position(0,0) #瀏覽器位置
driver.set_window_size(700,700) #瀏覽器大小
#點選場次
def e_click():
		try:
			# el = driver.find_elements_by_css_selector('.btn-next')
			# WebDriverWait(driver,20).until(ec.visibility_of_element_located((By.XPATH,"//input[@name='yt1' and @value='立即訂購']")))
			el = driver.find_elements_by_xpath("//input[@name='yt0' and @value='立即訂購']")
			print(len(el))
			#此範例為選擇第一場 以免有ERROR
			if(len(el)>0):
				el[0].click()
			else:
				print("redirect")
				time.sleep(0.5)
				driver.refresh()
					
		except Exception as e:
			print(e)
			raise
#選擇區域區
def choice_function():
		form_choice=None;
		try:
			#按照你想要的區域去選擇
			# form_choice = driver.find_element_by_xpath("//*[@id='group_1']/li[@class='select_form_a']")
			#尋找出還有空位的checkbox
			form_choice= driver.find_elements_by_xpath("//*[@id='group_6']/li/a[@*]")
			# for choice in form_choice:

			# 	print(choice.text)
			if(len(form_choice)>0):
				form_choice[-1].click()
			# else:
			# 	form_choice= driver.find_element_by_xpath("//*[@id='group_1']/li/a[@*]")
			# 	form_choice[-1].click()

			print("click choice")
		except Exception as e:

			print(e)
			raise
#選票數
def select_function():
	form_select = None
	try:

		# form_select =Select(driver.find_element_by_tag_name("select"))
		form_select = Select(WebDriverWait(driver,120).until(ec.visibility_of_element_located((By.TAG_NAME,'select'))))
		if form_select is not None:
			try:
				actions = ActionChains(driver)
				actions.click(driver.find_element_by_tag_name("select"))
				
				for option in form_select.options:
					if(option.text=='4'):
						option.click()
				actions.perform()
			except Exception as exc:
				print(exc)
				print("click mobile-select fail")
				pass
	except NoSuchElementException:
		print("find mobile-select fail")
#點選同意按鈕
def agree_function():
	form_checkbox = None
	try:
		# form_checkbox = driver.find_element_by_xpath("//*[@id='TicketForm_agree']")
		form_checkbox = WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='TicketForm_agree']")))
		if form_checkbox is not None:
			try:
				driver.execute_script("$('#TicketForm_agree').focus();")
				action_checkbox = ActionChains(driver)
				
				action_checkbox.click(form_checkbox)
				action_checkbox.perform()
				if not form_checkbox.is_selected():
					form_checkbox.click()
				# driver.execute_script("arguments[0].click();", form_checkbox)
				driver.execute_script("$('#TicketForm_agree').prop('checked', true);")
			except Exception as exc:
				print(exc)
				print("click TicketForm_agree fail")
				pass
	except NoSuchElementException:
		print("find TicketForm_agree fail")
	driver.execute_script("$('#TicketForm_verifyCode').focus();")

def main():
	while True:
		time.sleep(0.4)
		url=""
		try:
			url=driver.current_url
		except Exception as exc:
			pass
		if url is None:
			continue
		else:
			if len(url)==0:
				continue
			if ec.url_contains('detail')(driver):
				url = url.replace("detail","game")
				driver.get(url)
		print(url)
		if ec.url_contains('game')(driver):
			e_click();
		if ec.url_matches('https://tixcraft.com/ticket/area/*')(driver):
			choice_function();
		if ec.url_matches('https://tixcraft.com/ticket/ticket/*')(driver):
			select_function();
			agree_function();
			time.sleep(5)

if __name__=="__main__":
	main();




		

