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
# 发送链接请求，获取驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)

# ● 安装应用
# driver.install_app("app安装包的绝对路径")
# driver.install_app('./kfztt_113043.apk')

# ● 卸载应用
# driver.remove_app("app的包名")
# driver.remove_app("io.manong.developerdaily")

# ● 判断应用是否已经安装
# driver.is_app_installed("app的包名")
# driver.is_app_installed("io.manong.developerdaily")

# ● 获取当前操作的应用包名
curr_pack = driver.current_package
print(curr_pack)

# ● 获取当前操作的界面名字
curr_act = driver.current_activity
print(curr_act)

# ● 获取当前界面的 xml 源码
pave_xml = driver.page_source
print(pave_xml)


if driver.is_app_installed("io.manong.developerdaily"):
    print("开发者头条已安装，开始卸载...")
    driver.remove_app("io.manong.developerdaily")
    print("卸载完成！")
else:
    print("开发者头条未安装，开始安装...")
    driver.install_app(r'D:\WorkSpace\PythonTestCode\f_AppiumBase\kfztt_113043.apk')
    print("安装完成！")






time.sleep(3)
# ● 关闭应用和断开链接
driver.quit()
