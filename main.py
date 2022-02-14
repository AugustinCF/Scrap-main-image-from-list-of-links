# Scrap-main-image-from-list-of-links
This script in written in python using selenium, scrape links and download in order brand "(1), brand (2)" also ignore  some errors 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.request
import wget
import pandas as pd
import glob
from selenium.webdriver.common.keys import Keys
from urllib.error import HTTPError

logoforerror = 'https://www.zxc.cx/logo-300x235.jpg'

# links_list = pd.read_excel(r"C:\links.xlsx", sheet_name="Sheet1")
# print(links_list)

links_list = [

    "https://www.google.com/img/cxz, https://www.google.com/img/zxc]

for link in links_list:
    driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
    driver.implicitly_wait(15)
    print(link)
    driver.get(link)

    imgsrc = driver.find_elements_by_xpath('//*[@id="image"]')
    print(imgsrc)
    
    #used for to resolve attribute error
    for img in imgsrc:
        imaginea = img.get_attribute('src')

    try:
        prindeimaginea = wget.download(imaginea, out="catalog.png")


    except HTTPError:
        print("problma la imagine HTTPEror")
        wget.download(logoforerror, out="imgdown.png")
        continue

    print('Saved file: ', prindeimaginea)
    
    #if you want you urllib
    # urllib.request.urlretrieve(imgsrc, "C:\webdriver\imagscrap.jpg")

    time.sleep(3)  

    driver.close()

print('pass')
