# from selenium.webdriver.common.action_chains import *
from selenium import webdriver
import time
import random
from PIL import Image

# 初始化浏览器
browser = webdriver.Chrome()

# 加载张大妈首页
browser.get('http://www.smzdm.com')

# 定位登录按钮，并模拟点击
button_login = browser.find_element_by_class_name('J_login_trigger')
button_login.click()

# 点击登录按钮后，在页面生成一个包含登录框的iframe，切换至该iframe
browser.switch_to_frame('J_login_iframe')

# 定位用户名和密码输入框，并键入用户名密码
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys('######')
password.send_keys('******')

# 定位登录按钮，模拟点击进行登录
button_submit = browser.find_element_by_id('login_submit')
button_submit.click()

# 隐式等待10s，若规定时间内后续节点未加载出来则抛出异常
browser.implicitly_wait(10)

# 定位签到按钮，模拟点击完成签到
sign_button = browser.find_element_by_class_name('J_punch')
sign_button.click()

# 退出浏览器
browser.quit()
