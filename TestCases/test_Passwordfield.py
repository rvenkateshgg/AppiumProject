import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("12345678909876543210123456789098765432101234567")
password_field = len(driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").text)
print(password_field)


if password_field <= 50:
  print(True)
else:
  print(False)
  print("Password should not exceed 50 characters")