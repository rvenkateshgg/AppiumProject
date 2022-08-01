import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Total']").click()
time.sleep(1)
graph = driver.find_element(AppiumBy.XPATH,"//android.widget.Image[@index='0']").text
print(graph)

