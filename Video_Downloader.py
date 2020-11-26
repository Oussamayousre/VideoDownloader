import time
from selenium import webdriver
import datetime
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VideoDownloader : 
    def __init__(self , link) : 
        self.link  = link
        
        self.driver = webdriver.Chrome(('./Desktop/chromedriver'))
        time.sleep(1) 
        self.login()
        
    def login(self) : 
        self.driver.get("https://fr.savefrom.net/1-youtube-video-downloader-4.html")
        time.sleep(3) 


        self.driver.find_element_by_id('sf_url').send_keys(self.link)
        time.sleep(1)
        self.driver.find_element_by_id('sf_submit').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])

        time.sleep(10) 
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a').click()
       # time.sleep(5)
       # self.driver.switch_to.window(self.driver.window_handles[0])
        # self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a').click()
       # time.sleep(1)


def main():

    Video_link = input("copy the video link you want to download in 720p quality   ")
    downloader = VideoDownloader(Video_link)
if __name__ == '__main__':
    main()