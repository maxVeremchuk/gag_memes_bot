# from bs4 import BeautifulSoup
# import requests

# def getdata(url): 
#     r = requests.get(url) 
#     return r.text 

# htmldata = getdata("https://9gag.com/top")
# soup = BeautifulSoup(htmldata, 'html.parser') 
# print(soup)
# # for item in soup.find_all('div'):
# #     print(item)

import redis_db

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://9gag.com/top"
  
def get_new_img():
    driver = webdriver.Chrome('./chromedriver') 
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    scroll_value = 0
    redis_url = redis_db.RedisURL()
    all_urls_in_db = redis_url.get_urls()
    no_upd = True

    new_img = ""
    while no_upd:
        scroll_value += 1000
        driver.execute_script(f"window.scrollTo(0, {scroll_value})") 
        time.sleep(2) 
        html = driver.page_source
        
        soup = BeautifulSoup(html, "html.parser")
        imgs = soup.find_all('img')
            
        for img in imgs:
            img_src = img.get('src')
            #https://img-9gag-fun.9cache.com/photo/aGzReY7_460s.jpg - correct url
            if img_src is None or img_src.endswith("300x158.jpg") or (not img_src.startswith("https://img-9gag-fun")):
                continue
            if img_src not in all_urls_in_db:
                redis_url.set_url(img_src)
                #print(img_src)
                no_upd = False
                new_img = img_src
    driver.close() 
    return new_img


#print(get_new_img())




