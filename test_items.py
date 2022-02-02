import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    basket = browser.find_element_by_css_selector('#add_to_basket_form>button[type="submit"]')
    #от ассерта нет смысла, разве что проверка старых знаний на то , чтобы вытащить атрибут type из кнопки
