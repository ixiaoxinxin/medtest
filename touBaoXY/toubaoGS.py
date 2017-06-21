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
sh = bk.sheet_by_name(u"tbGS")
nrows = sh.nrows

class touBao(unittest.TestCase):
        for i in range(sh.nrows):
            iedriver = os.path.abspath("C:\Program Files\Internet Explorer\IEDriverServer")
            os.environ[ "webdriver.ie.driver"] = iedriver
            browser = webdriver.Ie(iedriver)
            url= "http://172.16.4.247:27002"
            browser.get(url)
            browser.find_element_by_id( "j_username" ).clear()
            browser.find_element_by_name( "j_username" ).send_keys("gskhjl")
            browser.find_element_by_id( "j_password" ).clear()
            browser.find_element_by_name( "j_password" ).send_keys( "111111" )
            #点击登录按钮
            browser.find_element_by_xpath("//img[contains( @onclick,'loginCheck()')]" ).click()
            time.sleep(4)
            #登陆成功，打开在线投保页面
            browser.implicitly_wait(30)
            browser.switch_to_frame("nav")
            time.sleep(3)
            browser.find_element_by_link_text(u"投保管理").click()
            time.sleep(3)
            browser.find_element_by_link_text(u"在线投保").click()
            #填写会员注册信息
            time.sleep(3)
            browser.implicitly_wait(30) #切换frame之前必须添加此句代码
            browser.switch_to_default_content()
            browser.switch_to_frame("framecontent")
            time.sleep(2)
            browser.implicitly_wait(30)
            Select(browser.find_element_by_id("cityId")).select_by_visible_text(u"白银市")
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
            time.sleep(3)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(4)
            browser.find_element_by_name("productId").click()
            time.sleep(4)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/form/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(3)
            browser.find_element_by_id("chk4").click()
            time.sleep(3)
            browser.find_element_by_id("chk3").click()
            time.sleep(3)
            browser.find_element_by_id("chk1").click()
            time.sleep(3)
            browser.find_element_by_id("chk2").click()
            time.sleep(4)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/table[2]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(4)
            browser.find_element_by_id( "lastYearTreatCount" ).clear()
            browser.find_element_by_id( "lastYearTreatCount" ).send_keys(int(sh.cell_value(i,1)))
            time.sleep(3)
            browser.find_element_by_id( "leaveHospitalCount" ).clear()
            browser.find_element_by_id( "leaveHospitalCount" ).send_keys(int(sh.cell_value(i,2)))
            time.sleep(3)
            Select(browser.find_element_by_id("annualRevenue")).select_by_visible_text(sh.cell_value(i,3))
            time.sleep(3)
            browser.find_element_by_xpath("a//[contains(@onclick,'showUploadDialog()')]").click()
            time.sleep(3)
            browser.find_element_by_id( "formBedCount" ).clear()
            browser.find_element_by_id( "formBedCount" ).send_keys(int(sh.cell_value(i,4)))
            time.sleep(3)
            browser.find_element_by_id( "openBedCount" ).clear()
            browser.find_element_by_id( "openBedCount" ).send_keys(int(sh.cell_value(i,5)))
            time.sleep(3)
            #***********遍历语句柄开始************
            nowhandle=browser.current_window_handle#在这里得到当前窗口句柄
            aalhandles=browser.window_handles
            for handle in aalhandles:#在所有窗口中查找弹出窗口
                if handle!=nowhandle:
                    browser.switch_to_window(handle)#这两步是在弹出窗口中进行的操作，证明我们确实进入了
                    time.sleep(2)
                    browser.find_element_by_id("staffExcel").send_keys("E:\\staffExcel.xls")
                    time.sleep(2)
                    browser.find_element_by_xpath("/html/body/div[9]/div[11]/button[1]").click()
            browser.implicitly_wait(30)
            browser.switch_to_window(nowhandle)#返回到主窗口页面
            #***********遍历语句柄结束************
            time.sleep(3)
            browser.find_element_by_id( "startDate" ).clear()
            browser.find_element_by_id( "startDate" ).send_keys(xlrd.xldate.xldate_as_datetime(sh.cell_value(i,6),0).strftime('%Y-%m-%d'))
            time.sleep(3)
            browser.find_element_by_id( "endDate" ).clear()
            browser.find_element_by_id( "endDate" ).send_keys(xlrd.xldate.xldate_as_datetime(sh.cell_value(i,7),0).strftime('%Y-%m-%d'))
            time.sleep(3)
            Select(browser.find_element_by_id("insureProgramId")).select_by_visible_text(sh.cell_value(i,8))
            time.sleep(3)
            Select(browser.find_element_by_id("isPaper")).select_by_visible_text(sh.cell_value(i,9))
            time.sleep(3)
            browser.find_element_by_id( "postInfoPostcode" ).clear()
            browser.find_element_by_id( "postInfoPostcode" ).send_keys(int(sh.cell_value(i,10)))
            time.sleep(3)
            browser.find_element_by_id( "note6" ).clear()
            browser.find_element_by_id( "note6" ).send_keys(int(sh.cell_value(i,11)))
            time.sleep(3)
            browser.find_element_by_id( "note5" ).clear()
            browser.find_element_by_id( "note5" ).send_keys(int(sh.cell_value(i,12)))
            time.sleep(3)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/table/tbody/tr/td[2]/a[2]/img").click()
            browser.implicitly_wait(30)
            Select(browser.find_element_by_id("bedCountOption")).select_by_visible_text(sh.cell_value(i,13))
            time.sleep(3)
            calculateResult = browser.find_element_by_id("calculateResult")
            print calculateResult
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/table/tbody/tr/td[2]/a[2]/img").click()
            #提交保单#
            time.sleep(3)
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[6]/table/tbody/tr/td/table[3]/tbody/tr/td[2]/a[2]/img").click()
            time.sleep(5)
            browser.quit()
 
            
        
        
if __name__ == "__main__":
        for i in range(sh.nrows):  
                touBao