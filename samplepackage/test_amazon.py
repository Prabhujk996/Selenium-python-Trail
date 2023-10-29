
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    time.sleep(5)
    driver.find_element(By.ID,value="twotabsearchtextbox").send_keys("Iphone12")
    time.sleep(5)
    driver.quit()