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

Login_btn = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']")
location = Login_btn.location

x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(Login_btn.size,"\n")

SingUp_btn = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='SIGN UP']")
location = SingUp_btn.location
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(SingUp_btn.size,"\n")

driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='LOG IN']").click()
time.sleep(2)

email_field = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']")
location = email_field.location
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(email_field.size,"\n")

password_field = driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]")
location = password_field.location
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(password_field.size,"\n")

login_btn = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']")
location = login_btn.location
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(login_btn.size,"\n")

eye_icon = driver.find_element(AppiumBy.XPATH,"//android.widget.Image[@text='eye outline']")
location = eye_icon.location
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(eye_icon.size,"\n")

forget_pass = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Forgot your password?']")
location = forget_pass.location
print(forget_pass.text)
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(forget_pass.size,"\n")

welcome_text = driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='Welcome Back!']")
location = welcome_text.location
print(welcome_text.text)
x = location.get('x')
print("x location:", x)
y = location.get('y')
print("y location:", y)
print(welcome_text.size,"\n")

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("venkateshrv307@gmail.com")
driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("123456")
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()

driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='History History']").click()

Dec = driver.find_element(AppiumBy.XPATH,"//android.view.View[@index='0']")
print(Dec.size)
Dec.click()
driver.back()

Nov = driver.find_element(AppiumBy.XPATH,"(//android.view.View[@index='0'])[1]")
print(Nov.size)
Nov.click()
driver.back()
