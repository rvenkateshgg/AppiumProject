import time
from appium import webdriver
from utilities import XlUtils
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
time.sleep(2)

path = "/Users/venkateshr/Desktop/Wg_email_datas.xlsx"
rows = XlUtils.getRowcount(path, 'Sheet1')
print(rows)

for r in range(2, rows + 1):
  username = XlUtils.readData(path,'Sheet1', r, 1)
  password = XlUtils.readData(path,'Sheet1', r, 2)

  driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
  time.sleep(2)

  username1 = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']")
  username1.clear()
  username1.send_keys(username)
  time.sleep(1)

  password1 = driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]")
  password1.clear()
  password1.send_keys(password)

  login_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LOG IN']").is_enabled()
  print("enable is:" + str(login_btn))

  login_btn1 = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LOG IN']")
  login_btn1.click()

  try:
    Actual_error_message = driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='Must use a valid email']").text
    if Actual_error_message == "Must use a valid email":
      print(Actual_error_message)
      print("Invalid Email address:", username)
      print("Pass","\n")
      XlUtils.writeData(path,'Sheet1',r,3, "Test Passed")

  except:
    print("Valid Email address:", username)
    print("Fail","\n")
    XlUtils.writeData(path,'Sheet1',r,3, "Test Failed")



