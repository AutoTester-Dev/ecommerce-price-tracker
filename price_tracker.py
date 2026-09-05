import requests
from bs4 import BeautifulSoup
import pandas as pd

# Test uchun xalqaro onlayn kitob do'koni
url = 'http://books.toscrape.com/'
response = requests.get(url)

products_data = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        products_data.append({
            'Product Name': title,
            'Price': price,
            'Availability': availability
        })
        
    df = pd.DataFrame(products_data)
    
    # Excel faylga saqlaymiz
    file_name = 'ecommerce_price_tracker.xlsx'
    df.to_excel(file_name, index=False)
    print("Birinchi loyiha muvaffaqiyatli tayyorlandi va Excel'ga saqlandi!")
    display(df.head())
else:
    print("Xatolik:", response.status_code)
