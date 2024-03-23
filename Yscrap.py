from bs4 import BeautifulSoup
import requests
import pandas as pd

res = requests.get('https://jiji.com.et/mobile-phones')
data = res.text

soup = BeautifulSoup(data, 'html.parser')

mobile_salaries = []
mobiles = []

for div in soup.find_all("div",class_="b-list-advert-base__data__header"):
    salary = div.find(name = 'div', class_="qa-advert-price").text.strip()
    mobile = div.find(name='div', class_='b-advert-title-inner qa-advert-title b-advert-title-inner--div').text.strip()
    combine = str(mobile) + ' - ' + str(salary)
    mobile_salaries.append(combine)
    
    
split_data = [item.split(' - ') for item in mobile_salaries]


df = pd.DataFrame(split_data, columns=['Device', 'Price'])
max_price = df['Price'].max()


price = [int(price.split(' - ')[1].split()[1].replace(',', '')  ) for price in mobile_salaries]

max_price = max(price)
print(max_price)