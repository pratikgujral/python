# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 06:58:55 2016

@author: prati
"""

# Selenium
import time
from selenium import webdriver

prof = webdriver.FirefoxProfile()
prof.set_preference("browser.startup.homepage_override.mston‌​e", "ignore")
prof.set_preference("startup.homepage_welcome_url.additional‌​", "about:blank")
driver = webdriver.Firefox(prof)
driver.get('http://seleniumhq.org/')
#time.sleep(5)
#driver.quit()

