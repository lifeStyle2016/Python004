from selenium import webdriver
import time

try :
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    time.sleep(2)
    # 用户名
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18811110000')
    # 密码
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('123456')
    time.sleep(2)
    # 点击登录
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
except Exception as e:
    print(f'登录失败：{e}')
finally:
    browser.close()