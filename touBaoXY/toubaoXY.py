#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import xlrd


#读取测试数据
fname = "E:\\testInfo\\tbInfo.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
sh = bk.sheet_by_name(u"tbXY")
nrows = sh.nrows

class touBao(unittest.TestCase):
        for i in range(sh.nrows):
            iedriver = os.path.abspath("C:\Program Files\Internet Explorer\IEDriverServer")
            os.environ[ "webdriver.ie.driver"] = iedriver
            browser = webdriver.Ie(iedriver)
            url= "http://172.16.4.247:27002"
            browser.get(url)
            browser.maximize_window()
            browser.find_element_by_id( "j_username" ).clear()
            browser.find_element_by_name( "j_username" ).send_keys("sxxykhjl")
            browser.find_element_by_id( "j_password" ).clear()
            browser.find_element_by_name( "j_password" ).send_keys( "111111" )
            #点击登录按钮
            browser.find_element_by_xpath("//img[contains( @onclick,'loginCheck()')]" ).click()
            time.sleep(2)
            #登陆成功，打开在线投保页面
            browser.implicitly_wait(30)
            browser.switch_to_frame("nav")
            browser.implicitly_wait(30)
            browser.find_element_by_link_text(u"投保管理").click()
            browser.implicitly_wait(30)
            browser.find_element_by_link_text(u"在线投保").click()
            #填写会员注册信息
            browser.implicitly_wait(30) #切换frame之前必须添加此句代码
            browser.switch_to_default_content()
            browser.switch_to_frame("framecontent")
            time.sleep(2)
            Select(browser.find_element_by_id("cityId")).select_by_visible_text(u"咸阳市")
            time.sleep(2)
            browser.find_element_by_id("word").clear()
            browser.find_element_by_id("word").send_keys(sh.cell_value(i,0))
            time.sleep(2)
            kw = browser.find_element_by_id("auto")#找到模糊查询结果显示的位置
            time.sleep(2)
            ActionChains(browser).click(kw).perform()#由于是精确输入，所以只会显示一条记录，点击词条记录
            time.sleep(2) 
            browser.find_element_by_xpath("//img[contains(@id,'ok')]" ).click()#点击确定进入下一步
            time.sleep(2)  
            browser.find_element_by_name("operSalemanInfo.salemanId").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(2)
            browser.find_element_by_name("productId").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/form/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(2)
            browser.find_element_by_id("chk4").click()
            time.sleep(2)
            browser.find_element_by_id("chk3").click()
            time.sleep(2)
            browser.find_element_by_id("chk1").click()
            time.sleep(2)
            browser.find_element_by_id("chk2").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(2)
            browser.find_element_by_id( "lastYearTreatCount" ).clear()
            browser.find_element_by_id( "lastYearTreatCount" ).send_keys(int(sh.cell_value(i,1)))
            time.sleep(2)
            browser.find_element_by_id( "lastYearInHospitalCount" ).clear()
            browser.find_element_by_id( "lastYearInHospitalCount" ).send_keys(int(sh.cell_value(i,2)))
            time.sleep(2)
            browser.find_element_by_id( "lastYearSurgeryCount" ).clear()
            browser.find_element_by_id( "lastYearSurgeryCount" ).send_keys(int(sh.cell_value(i,3)) )
            time.sleep(2)
            browser.find_element_by_id( "startDate" ).clear()
            browser.find_element_by_id( "startDate" ).send_keys(xlrd.xldate.xldate_as_datetime(sh.cell_value(i,4),0).strftime('%Y-%m-%d'))
            time.sleep(2)
            browser.find_element_by_id( "endDate" ).clear()
            browser.find_element_by_id( "endDate" ).send_keys(xlrd.xldate.xldate_as_datetime(sh.cell_value(i,5),0).strftime('%Y-%m-%d'))
            time.sleep(2)
            browser.find_element_by_id( "annualRevenueYear" ).clear()
            browser.find_element_by_id( "annualRevenueYear" ).send_keys(sh.cell_value(i,6))
            time.sleep(2) 
            browser.find_element_by_id("basePolicyfeeId").click()
            Select(browser.find_element_by_id("basePolicyfeeId")).select_by_visible_text(sh.cell_value(i,7))
            time.sleep(2)
            Select(browser.find_element_by_id("compenstateLimitYZInfoId")).select_by_visible_text(sh.cell_value(i,8))
            time.sleep(2)
            Select(browser.find_element_by_id("isPaper")).select_by_visible_text(sh.cell_value(i,9))
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/table/tbody/tr/td[2]/a[2]/img").click()
            browser.implicitly_wait(30)
            time.sleep(2)
            browser.find_element_by_class_name("btn").click()
            time.sleep(2)
            #点击计算保费并打印
            calculateResult = browser.find_element_by_id("calculateResult")
            print calculateResult
            time.sleep(2)
            browser.get_screenshot_as_file("E://testSY//"+sh.cell_value(i,0)+str(int(sh.cell_value(i,10)))+".png")
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/table/tbody/tr/td[2]/a[2]/img").click()
            #提交保单#
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[6]/table/tbody/tr/td/table[3]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(2)
            browser.get_screenshot_as_file("E://testSY//"+sh.cell_value(i,0)+"Num"+str(int(sh.cell_value(i,10)))+".png")
            time.sleep(3)
            browser.quit()
 
            
        
        
if __name__ == "__main__":
        for i in range(sh.nrows):  
                touBao