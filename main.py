# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                          options=None)
driver.get("https://segmentfault.com/a/1190000015642808")
try:
    current_web_id = driver.find_element_by_id("item-1")
    print("type: %s" % type(current_web_id))
    print("Class instance: %s" % current_web_id)
    print("id: item-1; content: %s" % current_web_id.text)
finally:
    driver.close()
