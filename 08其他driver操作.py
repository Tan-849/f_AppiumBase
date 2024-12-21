# appium 是由 selenium 团队二次开发的 app 自动化第三方库
# appium 基于 selenium
# app 自动化测试跟 web 自动化唯一的区别：
# app 测试的是手机程序界面
# web 测试的是网站的页面
import time
from time import sleep

# 导包
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# 配置手机的连接参数信息(利用字典)
desired_cap={}
# 设备名
desired_cap['deviceName']='127.0.0.1:62001'
# 系统名
desired_cap['platformName']='Android'
# app名
desired_cap['appPackage']='com.android.settings'
# app界面名
desired_cap['appActivity']='.Settings'
# 发送链接请求，获取驱动对象，打开设置
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)

# 获取时间
print(driver.device_time)
# 获取分辨率
print(driver.get_window_size())
# 获取手机的网络信息
print(driver.network_connection)
# 设置网络信息
driver.set_network_connection(6) # 已经开启的网络不会重复开启
print(driver.network_connection)
# 打开手机通知栏
sleep(2)
driver.open_notifications()
# 截图
driver.save_screenshot('./screenshot.png')




time.sleep(5)
driver.quit()
