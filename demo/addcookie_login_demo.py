# coding=gbk
# 上行解决编码报错(报错内容:SyntaxError: Non-UTF-8 code starting with '\xb9' in file,出错的根源就是代码中有中文注释导致编码问题)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 登录唯爱优选管理系统
driver.get("http://wa.demo.sclonsee.com/")
driver.maximize_window()

# 通过添加Cookie跳过登录验证直接登录(前提是Cookie不失效):
# 1，可以先通过抓包工具等获取Cookie
# 2，通过Selenium提供的add_cookie()方法添加Cookie信息,多条Cookie分多次添加
driver.add_cookie({"name": "advanced-backend", "value": "9dv872hpqagg0pbq1rsn5a7i53"})
driver.add_cookie({"name": "_identity-backend",
                   "value": "0007be3bc00303df5e8948e39a7528adbb4027892890c531425096f01c7cabdaa%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity-backend%22%3Bi%3A1%3Bs%3A43%3A%22%5B1%2C%22hRJ6Az_SgAckqltCzUSEcGEuDv1MfbsT%22%2C7200%5D%22%3B%7D"})
driver.add_cookie({"name": "_csrf-backend",
                   "value": "80b39f8d26989b28828a01ccf0909635833e38f33674102bbb1d7520f441cf71a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_csrf-backend%22%3Bi%3A1%3Bs%3A32%3A%22o302IcjERYZSmVH3bUwWu1OG9z_BU29G%22%3B%7D"})

sleep(3)
driver.refresh()
# 刷新页面，查看是否登录成功
sleep(3)

# 获取登录用户名并打印
username = driver.find_element(by=By.CLASS_NAME, value="hidden-xs").text
print(username)

# 关闭浏览器
driver.quit()

# WebDriver常用操作Cookie的方法有：
# get_cookies():获取所有的Cookie
# get_cookie(name):返回字典中key为name的Cookie
# add_cookie(dict):添加Cookie
# delect_cookie(name, optionString):删除名为optionString的Cookie
# delect_all_cookies():删除所有Cookie
