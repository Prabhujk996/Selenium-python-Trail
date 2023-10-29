import time

from selenium import webdriver


def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    time.sleep(10)
    driver.quit()


def test_tutorial_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://titorialsninja.com/demo/")
    time.sleep(5)
    driver.quit()


def test_selenium_143():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium143.blogspot.com/")
    time.sleep(5)
    driver.quit()


