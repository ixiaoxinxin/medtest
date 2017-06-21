#-*- coding: utf8 -*-
import xlrd

fname = "E:\\userInfo.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name(u"testInfoSY")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
#获取第N行第N个单元的数据,将每列数据写入页面上的输入框
for i in range(nrows):
    loginName = sh.cell_value(i,0)
    password = int(sh.cell_value(i,1))
    passwordConfirm = int(sh.cell_value(i,2))
    hospitalName = sh.cell_value(i,3)
    registeredAddress = int(sh.cell_value(i,4))
    cityCodeOper = sh.cell_value(i,5)
    areaCodeOper = sh.cell_value(i,6)
    postcode = sh.cell_value(i,7)
    lawMan = sh.cell_value(i,8)
    owershipType = sh.cell_value(i,9)
    note = sh.cell_value(i,10)
    levelOneCodes = sh.cell_value(i,11)
    levelTwoCodes = sh.cell_value(i,12)
    surgeryId  = sh.cell_value(i,13)
    mliTypePara = sh.cell_value(i,14)
    orgLicenseNo = int(sh.cell_value(i,15))
    orgLicenseNoCFile = sh.cell_value(i,16)
    organizationCode = int(sh.cell_value(i,17))
    organizationCodeFile = sh.cell_value(i,18)
    businessLicenseNo = int(sh.cell_value(i,19))
    businessLicenseNoFile = sh.cell_value(i,20)
    name = sh.cell_value(i,21)
    telephone  = int(sh.cell_value(i,22))
    email = sh.cell_value(i,23)
    print  loginName, password,passwordConfirm,hospitalName,registeredAddress,cityCodeOper ,areaCodeOper,lawMan,owershipType ,note,levelOneCodes,levelTwoCodes,surgeryId ,mliTypePara,orgLicenseNo,orgLicenseNoCFile,organizationCode,  organizationCodeFile,businessLicenseNo,businessLicenseNoFile,name,telephone, email
 



