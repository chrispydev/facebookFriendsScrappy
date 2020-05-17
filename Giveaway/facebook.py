import os
import time
from selenium import webdriver
from credentials import LOGIN, PASSWORD
import re


class Giveaway:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.path = f'{os.getcwd()}/chromedriver'
        self.driver = webdriver.Chrome(self.path)

    def login(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        element = driver.find_element_by_xpath('//*[@id="email"]')
        element.send_keys(self.username)
        element = driver.find_element_by_xpath('//*[@id="pass"]')
        element.send_keys(self.password)
        time.sleep(2)
        element.submit()
        time.sleep(2)

    def friends(self):
        self.driver.get('https://www.facebook.com/chris.owusu.712')
        time.sleep(2)
        self.driver.get(
            'https://www.facebook.com/chris.owusu.712/friends?lst=100006702310417%3A100006702310417%3A1589669573&source_ref=pb_friends_tl')
        time.sleep(20)
        try:
            friends_btn = self.driver.find_element_by_class_name('_gs6')
            total_friends = friends_btn.get_attribute('textContent')
            time.sleep(1)
            print('Finding the total number of friends.....')
            print(f'This is the total friends number: {total_friends}')
        except Exception:
            print('Unable to locate the element')

    def close_browser(self):
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    fb = Giveaway(LOGIN, PASSWORD)
    fb.login()
    fb.friends()
    fb.close_browser()
