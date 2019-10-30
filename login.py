from selenium import webdriver

usr = "YOUR USERNAME (ROLL NO )"
pwd = "YOUR PASSWORD"

driver = webdriver.Chrome("ENTER THE PATH")
driver.get('https://172.16.1.1:8090/httpclient.html?u={proto}{url}')

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('logincaption')
login_btn.submit()
