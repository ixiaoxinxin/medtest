#-*- coding: UTF-8 -*-
from selenium import webdriver
import os,time
from selenium.webdriver.support.ui import Select

iedriver = os.path.abspath("C:\Program Files\Internet Explorer\IEDriverServer")
os.environ["webdriver.ie.driver"] = iedriver
browser = webdriver.Ie(iedriver)
url = "http://172.16.4.127:27002/"
browser.get(url)
browser.find_element_by_name("j_username").clear()
browser.find_element_by_name("j_username").send_keys("jt-tj")
browser.find_element_by_name("j_password").clear()
browser.find_element_by_name("j_password").send_keys("111111")
browser.find_element_by_xpath("html/body/center/table[1]/tbody/tr/td/div/table[2]/tbody/tr/td[1]/table/tbody[2]/tr[3]/td/table/tbody/tr/td[1]/a/img").click()
browser.implicitly_wait(30)
browser.switch_to.frame("nav")
time.sleep(1)
browser.find_element_by_link_text(u"用户管理").click()
time.sleep(1)
browser.find_element_by_link_text(u"会员注册").click()
time.sleep(1)
browser.switch_to.default_content()
time.sleep(1)
browser.switch_to.frame("framecontent")
time.sleep(1)
browser.find_element_by_id("provinceName").click()
time.sleep(1)
Select(browser.find_element_by_id("provinceId")).select_by_visible_text(u"北京市")