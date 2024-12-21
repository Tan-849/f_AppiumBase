# appium 是由 selenium 团队二次开发的 app 自动化第三方库
# appium 基于 selenium
# app 自动化测试跟 web 自动化唯一的区别：
# app 测试的是手机程序界面
# web 测试的是网站的页面
import time
from time import sleep

# 导包
from appium import webdriver
from selenium.webdriver.common.by import By

# 配置手机的连接参数信息(利用字典)
desired_cap={}
# 设备名
desired_cap['deviceName']='127.0.0.1:62001'
# 系统名
desired_cap['platformName']='Android'
# app名
desired_cap['appPackage']='com.android.launcher3'
# app界面名
desired_cap['appActivity']='.launcher3.Launcher'
# 发送链接请求，获取驱动对象，打开设置
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
el1 = driver.find_element(By.XPATH,'//*[@text="浏览器"]')
el2 = driver.find_element(By.XPATH,'//*[@text="谷歌安装器"]')
driver.drag_and_drop(el1,el2)
# el1 = [592,700]

time.sleep(5)
driver.quit()
