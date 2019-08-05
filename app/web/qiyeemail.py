from selenium import webdriver

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://exmail.qq.com/cgi-bin/loginpage?t=dm_loginpage&s=logout")
driver.find_element_by_id("inputuin").send_keys("yanyan.li@igen-tech.com")
driver.find_element_by_id("pp").send_keys('Wtf987901')
driver.find_element_by_id("btlogin").click()

# driver.find_element_by_id("readmailbtn_link").click()
driver.find_element_by_id("folder_6").click()
driver.switch_to.frame("iframe#mainFrame")
driver.find_element_by_id()


