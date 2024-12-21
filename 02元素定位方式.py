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
# 连接手机最基本的参数：设备，系统，app，界面

# 发送链接请求，获取驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)

# 定位元素，操作元素
# driver.find_element(By.XPATH,'//*[@text="显示"]').click()
# driver.find_element(By.XPATH,'//*[@text="声音"]').click()
# sleep(1)
# driver.find_element(By.XPATH,'//*[@text="手机铃声"]').click()

# 定义当前界面之外的元素
# app界面为了保证内存利用率，仅仅加载所有可操作的元素到内存中
# 如果 app 界面进行了切换，只能操作当前界面的元素
# driver.find_element(By.XPATH,'//*[@text="安全"]').click() # 找不到该元素

# 根据坐标定位元素
# 定位 声音元素
driver.tap([(108,1211)],duration=1000)

time.sleep(3)
driver.quit()
