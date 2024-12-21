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


# 通过事件链的方式进行滚动操作
action = TouchAction(driver)
el1 = driver.find_element(By.XPATH, '//*[@text="设置"]')
el2 = driver.find_element(By.XPATH, '//*[@text="通知"]')
# press 短按
# wait 短按时长，单位ms
# move_to 移动到
action.press(el2).wait(200).move_to(el1)
# 事件链操作完成之后松手
action.release()
# 提交事件链
action.perform()

# 点击安全
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="安全"]').click()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="屏幕锁定"]').click()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="图案"]').click()
sleep(0.5)
action.press(x=140,y=610).wait(200).move_to(x=580,y=610).wait(200).move_to(x=580,y=1040).wait(200).release()
action.perform()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="继续"]').click()

action.press(x=140,y=610).wait(200).move_to(x=580,y=610).wait(200).move_to(x=580,y=1040).wait(200).release()
action.perform()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="确认"]').click()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@text="完成"]').click()


time.sleep(5)
driver.quit()
