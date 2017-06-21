#-*- coding: UTF-8 -*-
from selenium import webdriver
import unittest
import time
import os



iedriver = os.path.abspath(r"C:\Program Files\Internet Explorer\IEDriverServer")
os.environ["webdriver.ie.driver"] = iedriver
browser = webdriver.Ie(iedriver)


class login(unittest.TestCase):
    url="http://172.16.4.247:27002"
    url_main="http://172.16.4.247:27002/main.jsp"    
    browser.get(url)
    browser.find_element_by_id( "j_username").clear()
    browser.find_element_by_name( "j_username" ).send_keys("sxxykhjl")
    browser.find_element_by_id( "j_password").clear()
    browser.find_element_by_name( "j_password" ).send_keys("111111" )
  
    #点击登录按钮
    browser.find_element_by_xpath( "/html/body/table[5]/tbody/tr/td[7]/table/tbody/tr[1]/td/form/table/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/a/img").click()
    browser.implicitly_wait(30)
    browser.get(url_main)
    browser.switch_to_frame("nav")
    browser.find_element_by_link_text(u"会员管理").click()
    time.sleep(1)
    browser.find_element_by_link_text(u"会员注册") .click()
    time.sleep(1)
  
if __name__ == "__main__":
    unittest.main()
  
