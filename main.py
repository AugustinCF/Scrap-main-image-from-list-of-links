from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import urllib.request
import wget
from urllib.error import HTTPError

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

logoddi = 'https://xyz.foo/sd-logo-300x235.jpg'

links_list = [
 #here links
]



for link in links_list:
    driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
    #driver = webdriver.Firefox('C:\webdriver\geckodriver.exe')


    driver.implicitly_wait(15)
    print(link)
    driver.get(link)

    imgsrc = driver.find_elements_by_xpath('//*[@id="product"]/ul[1]/li[2]/a/img')
    #print(imgsrc)
    time.sleep(3)
    def imaginea():
        print()

    for img in imgsrc:
        imaginea = img.get_attribute('src')

    try:
        prindeimaginea = wget.download(imaginea, out="brand.jpg")


    except urllib.error.HTTPError as e:
        print (e,"HTTPhorror")
        HTTPhorror = wget.download(logoddi, out="brand.jpg")
        print("Fisier salvat Rev",HTTPhorror)
        continue
    except urllib.error.URLError as e:
        print(e,"UrlHorror")
        UrlHorror = wget.download(logoddi, out="brand.jpg")
        print("Fisier salvat Rev",UrlHorror)
        continue
    except AttributeError as e:
        print(e,"AttHorror Pagina nu exista")
        AttHorror = wget.download(logoddi, out="brand.jpg")
        print("Fisier salvat Rev",AttHorror)
        continue

    # imgbrandget = wget.download(imgbrand, out="brand.jpg")

    print('Fisier salvat: ', prindeimaginea)

    # urllib.request.urlretrieve(imgsrc, "C:\webdriver\imaginescrap.jpg")

    time.sleep(3)  # required for my usage

    driver.close()

print('pass')
