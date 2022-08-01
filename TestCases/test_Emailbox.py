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

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("email@1234567890.com123456789015448415455555454151512354812335447886112345678998765432112345698745678")
email_input = len(driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").text)
print(email_input)

if email_input <= 100:
  print("True")
else:
  print("False")
  print("Email should not exceed 100 characters")

