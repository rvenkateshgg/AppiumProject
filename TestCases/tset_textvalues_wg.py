import time
import logging as L
import inspect
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
"""
Desired Capabilities:
"""

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "uiautomator2",
  "appium:app": "/Users/venkateshr/Desktop/App/Android/WG-4.1.0-Release.apk",
  "appPackage": "com.dmdbrands.gurus.weight",
  "appActivity": "com.dmdbrands.gurus.weight.MainActivity",
  "appium:noReset": "true"
}
# set driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
time.sleep(1)

driver.save_screenshot('weight_guru.png')
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
time.sleep(2)
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("venkateshrv307@gmail.com")
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("123456")
time.sleep(1)
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LOG IN']").click()
time.sleep(3)

element = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='187.4 lbs']").text
print(element)
element1 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='--%Body Fat']").text
print(element1)
element2 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='--%Muscle Mass']").text
print(element2)
element3 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='--%Water Weight']").text
print(element3)
element4 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='19.6BMI']").text
print(element4)
element5 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Week']").text
print(element5)
element6 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Month']").text
print(element6)
element7 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Year']").text
print(element7)
element8 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Total']")
print(element8.text)
element8.click()
element9 = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='Dashboard Dashboard']").text
print(element9)
element10 = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='ManualEntry Manual Entry']").text
print(element10)
element11 = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='History History']").text
print(element11)
element12 = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='Settings Settings']").text
print(element12)

driver.save_screenshot('weight_gurus1.png')

