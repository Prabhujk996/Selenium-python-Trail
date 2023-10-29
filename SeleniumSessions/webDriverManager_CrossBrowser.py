import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
time.sleep(2)
"""
driver.find_element(By.ID,"drop1").click()
driver.find_element(By.ID, "ta1").send_keys("Hello bro,\ni love my baby")
driver.find_element(By.NAME, "q").send_keys("hello world")
driver.find_element(By.NAME, "pswrd").send_keys("hello world")
 ++ storing the elements to perform multiple operations on same++
text_field_one = driver.find_element(By.ID, "textbox1")
text_field_one.clear()
time.sleep(2)
text_field_one.send_keys("Prabhu")
time.sleep(2)
text_field_one.clear()
time.sleep(2)
text_field_one.send_keys("kumar")

text_of_element = driver.find_element(By.ID, "pah").text
print(text_of_element)

driver.quit()
  ++@HTML Tags++
button_of_labble = driver.find_element(By.ID, "button9").text
print(button_of_labble)
"""
