import requests
import os
from selenium import webdriver
import time
import subprocess


def connect():
    driver = webdriver.Firefox()
    new_url = 'http://auth4.tsinghua.edu.cn'
    driver.get(new_url)
    try:
        driver.find_element_by_id('username').send_keys('用户名')
        driver.find_element_by_id('password').send_keys('密码')
        time.sleep(2)
        driver.find_element_by_name('connect').click()
        time.sleep(2)
        driver.quit()
    except:
        try:
            time.sleep(2)
            driver.find_element_by_class_name('disconnect').click()
            time.sleep(2)
            driver.quit()
            driver = webdriver.Firefox()
            driver.get(new_url)
            driver.find_element_by_id('username').send_keys('用户名')
            driver.find_element_by_id('password').send_keys('密码')
            time.sleep(2)
            driver.find_element_by_name('connect').click()
            time.sleep(2)
            driver.quit()
        except:
            pass


if __name__ == '__main__':
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping baidu.com',
                              shell=True,
                              stdout=fnull,
                              stderr=fnull)
    if return1:
        connect()