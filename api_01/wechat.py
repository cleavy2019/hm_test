from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://cn.bing.com/')
time.sleep(2)
driver.get('http://www.baidu.com')
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.find_element_by_id('kw').send_keys("qq邮箱")
driver.find_element_by_id('su').click()
time.sleep(3)
a = driver.current_window_handle
print(a)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
b = driver.window_handles
print(b)
for i in b:
    if i != a:
        driver.switch_to.window(i)
        print(i)
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').send_keys('1667037210')
        driver.find_element_by_id('p').send_keys('weilong01060416')
        driver.find_element_by_id('login_button').click()
        time.sleep(5)
        html = driver.page_source
        file = open("C:\\Users\\Administrator\\Desktop\\abc.html",'w')
        file.write(html)
        driver.close()
        time.sleep(2)
driver.quit()


