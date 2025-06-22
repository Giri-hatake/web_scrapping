import requests
from bs4 import BeautifulSoup as bs
import pandas as pd  

r = requests.get('https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000')
print(r)
s = bs(r.text, 'html.parser')
mobile_name = s.find_all('div', {'class': 'KzDlHZ'})
price_detials = s.find_all('div', {'class': 'Nx9bqj _4b5DiR'})

number = 0


data = []

for i in mobile_name:
    print(mobile_name[number].text)
    print(price_detials[number].text)

    
    data.append({
        'Mobile Name': mobile_name[number].text,
        'Price': price_detials[number].text
    })

    number = number + 1 

# Saving the datas to Excel
df = pd.DataFrame(data)
df.to_excel(r'D:\python_1\web_scraping\web_scraping_result.xlsx', index=False)

print("web_scraping_result.xlsx")
