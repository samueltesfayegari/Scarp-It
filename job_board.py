import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



service = Service(executable_path='chromedriver.exe')
url = 'https://www.naukri.com/top-jobs-by-designations'

driver = webdriver.Chrome(service=service)
driver.get(url)


time.sleep(5)


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
all_divs = soup.find('div', {'id': 'nameSearch'})
job_profiles = all_divs.find_all('a')


count = 0

for job_profile in job_profiles:
    print(job_profile.text)
    count = count + 1
    # if(count == 10):
    #     break
    
print(count)    
driver.close()
