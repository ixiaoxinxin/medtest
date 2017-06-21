#-*- coding: UTF-8 -*-
from selenium import webdriver
import os
import time
import unittest
from selenium.webdriver.support.ui import Select

iedriver = os.path.abspath("C:\Program Files\Internet Explorer\IEDriverServer")
os.environ[ "webdriver.ie.driver"] = iedriver
browser = webdriver.Ie(iedriver)

class Register(unittest.TestCase):
    url= "http://172.16.4.247:27002/index.jsp"
    browser.get(url)
    browser.find_element_by_id( "j_username" ).clear()
    browser.find_element_by_name( "j_username" ).send_keys("sxxykhjl")
    browser.find_element_by_id( "j_password" ).clear()
    browser.find_element_by_name( "j_password" ).send_keys( "111111" )
    #点击登录按钮
    browser.find_element_by_xpath("/html/body/table[5]/tbody/tr/td[7]/table/tbody/tr[1]/td/form/table/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/a/img" ).click()
    time.sleep(4)
    #登陆成功，打开会员注册页面
    browser.implicitly_wait(30)
    browser.switch_to_frame("nav")
    time.sleep(3)
    browser.find_element_by_link_text(u"会员管理").click()
    time.sleep(2)
    browser.find_element_by_link_text(u"会员注册").click()
    time.sleep(3)
    #填写会员注册信息
    browser.implicitly_wait(30) #切换frame之前必须添加此句代码
    browser.switch_to_default_content()
    browser.switch_to_frame("framecontent")
    time.sleep(4)
    browser.find_element_by_xpath("//img[contains(@id,'welcomeRegOk')]" ).click()
    time.sleep(4)
    browser.find_element_by_id( "loginName" ).clear()
    browser.find_element_by_id( "loginName" ).send_keys('xianyang002')
    time.sleep(2)
    browser.find_element_by_id( "password" ).clear()
    browser.find_element_by_id( "password" ).send_keys('111111' )
    time.sleep(2)
    browser.find_element_by_id( "passwordConfirm" ).clear()
    browser.find_element_by_id( "passwordConfirm" ).send_keys('111111' )
    time.sleep(2)
    browser.find_element_by_id( "hospitalName" ).clear()
    browser.find_element_by_id( "hospitalName" ).send_keys(u"咸阳二级综合非营利zkx" )
    time.sleep(2)
    browser.find_element_by_id( "registeredAddress" ).clear()
    browser.find_element_by_id( "registeredAddress" ).send_keys('111111' )
    time.sleep(2)
    selectc = browser.find_element_by_id( "cityCodeOper" )
    allOptionsc = selectc.find_elements_by_tag_name("option" )
    for option in allOptionsc:
        if '咸阳市' in option.text:
            option.click()
    time.sleep(2)
    browser.find_element_by_id( "areaCodeOper" ).click()#点击一下下拉框刷新出该地区下的所有选项
    time.sleep(2)
    selecta = browser.find_element_by_id( "areaCodeOper" )
    allOptionsa = selecta.find_elements_by_tag_name("option" )
    for option in allOptionsa:
        if '彬县' in option.text:
            option.click()
    time.sleep(2)
    browser.find_element_by_id( "postcode").clear()
    browser.find_element_by_id( "postcode" ).send_keys('111111' )
    time.sleep(2)
    browser.find_element_by_id( "lawMan" ).clear()
    browser.find_element_by_id( "lawMan" ).send_keys('111111' )       
    time.sleep(2)
    browser.find_element_by_id( "areaCodeOper" ).click()#点击一下下拉框刷新出该地区下的所有选项
    time.sleep(2)
    Select(browser.find_element_by_id("owershipType")).select_by_visible_text(u"非营利")
    time.sleep(2)
    Select(browser.find_element_by_id("note")).select_by_visible_text(u"厅直厅管")
    time.sleep(2)
    selectl = browser.find_element_by_id( "levelOneCodes" )
    allOptionsl = selectl.find_elements_by_tag_name("option" )
    for option in allOptionsl:
        if '二级' in option.text:
            option.click()
    time.sleep(2)
    browser.find_element_by_id("levelTwoCodes" ).click() #点击一下下拉框刷新出该地区下的所有选项
    time.sleep(2)
    selectll = browser.find_element_by_id("levelTwoCodes" )
    allOptionsll = selectll.find_elements_by_tag_name("option" )
    for option in allOptionsll:
        if '甲等' in option.text:
            option.click()
    time.sleep(2)
    Select(browser.find_element_by_id("surgeryId")).select_by_visible_text(u"是")
    time.sleep(2)
    Select(browser.find_element_by_id("mliTypePara")).select_by_visible_text(u"综合医院")
    time.sleep(2)
    browser.find_element_by_id( "orgLicenseNo" ).clear()
    browser.find_element_by_id( "orgLicenseNo" ).send_keys('12342452' )
    time.sleep(2)
    browser.find_element_by_id("orgLicenseNoCFile" ).clear()
    browser.find_element_by_id( "orgLicenseNoCFile" ).send_keys('E:\\1.jpg')
    time.sleep(2)
    browser.find_element_by_id("organizationCode" ).clear()
    browser.find_element_by_id( "organizationCode" ).send_keys('1212123116345435' )
    time.sleep(2)
    browser.find_element_by_id("organizationCodeFile" ).clear()
    browser.find_element_by_id( "organizationCodeFile" ).send_keys('E:\\1.jpg')
    time.sleep(2)
    browser.find_element_by_id("businessLicenseNo" ).clear()
    browser.find_element_by_id( "businessLicenseNo" ).send_keys('1212123634511435' )
    time.sleep(2)
    browser.find_element_by_id("businessLicenseNoFile" ).clear()
    browser.find_element_by_id( "businessLicenseNoFile" ).send_keys('E:\\1.jpg')
    time.sleep(2)
    browser.find_element_by_id( "name" ).clear()
    browser.find_element_by_id( "name" ).send_keys( 'zkx' )
    time.sleep(2)
    browser.find_element_by_id( "cellPhone" ).clear()
    browser.find_element_by_id( "cellPhone" ).send_keys('13811026904' )
    time.sleep(2)
    browser.find_element_by_id( "email" ).clear()
    browser.find_element_by_id( "email" ).send_keys('295563386@qq.com')
    browser.implicitly_wait(30)
    browser.find_element_by_id( "validateCode" ).clear()
    browser.implicitly_wait(30)
    browser.find_element_by_id("zcjc").click()
    browser.find_element_by_id("button").click()

if __name__ == "__main__":
    unittest.main()