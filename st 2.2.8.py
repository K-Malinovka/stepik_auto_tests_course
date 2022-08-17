from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os 

try:
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("div.form-group :nth-child(2)")
input1.send_keys("1")

input2 = browser.find_element_by_css_selector("div.form-group :nth-child(4)")
input2.send_keys("2")

input3 = browser.find_element_by_css_selector("div.form-group :nth-child(6)")
input3.send_keys("3")


current_dir = os.path.abspath(os.path.dirname(/Users/Katrine/selenium_course))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)


button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text


finally:
time.sleep(10)
browser.quit()