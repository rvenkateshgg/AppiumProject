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

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='SIGN UP']").click()
time.sleep(2)

Fname = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']")
Fname.send_keys("john")
print(Fname.size)

Lname = driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]")
Lname.send_keys("smith")
print(Lname.size)

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='NEXT']").click()

driver.find_element(AppiumBy.XPATH,"(//android.view.View[@index='0'])[1]").click()
