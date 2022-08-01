import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

"""
Desired Capabilities:
"""

desired_cap={
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

element = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@index='0']")
print(element.text)
element.click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("venkateshrv307@gmail.com")
time.sleep(1)
#driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("123")
#time.sleep(1)
login_btn = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").is_enabled()
print(login_btn)
icon = driver.find_element(AppiumBy.XPATH,"//android.widget.Image[@text='eye outline']").is_enabled()
print(icon)

#time.sleep(3)

#driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='Settings Settings']").click()

#actions = TouchAction(driver)
#actions.press(x=511, y=1891).move_to(x=507, y=952).release().perform()
#time.sleep(4)

#driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='Log Out']").click()
#time.sleep(2)

#driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG OUT']").click()
#time.sleep(4)
#driver.quit()
#print("Log out successfully")
