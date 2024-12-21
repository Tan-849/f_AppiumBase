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
desired_cap['appPackage']='com.android.settings'
# app界面名
desired_cap['appActivity']='.Settings'
# 发送链接请求，获取驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)

el1 = driver.find_element(By.ID,'com.android.settings:id/search')
# ● 获取元素的文本内容
print(el1.text)
# ● 获取元素的属性值
print(el1.get_attribute("class"))
# ● 获取元素的坐标
print(el1.location)
# ● 获取元素的宽高（大小）
print(el1.size)
# ● 对元素进行点击操作
el1.click()
el2 = driver.find_element(By.ID,'android:id/search_src_text')
# ● 对元素进行输入操作
el2.send_keys("显示")






time.sleep(3)
# ● 关闭应用和断开链接
driver.quit()
