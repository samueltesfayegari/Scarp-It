from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetching the webpage content
res = requests.get('https://www.1688.com/')
data = res.text

# Parsing the HTML content
soup = BeautifulSoup(data, 'html.parser')

# Creating lists to store data
products = []
prices = []
variants = []
descriptions = []
reviews = []

# Finding product details
for item in soup.find_all("div", class_="sm-offer-item"):
    # Product name
    product = item.find("a", class_="sm-offer-photoLink sw-dpl-offer-photoLink")['title']
    products.append(product)

    # Price
    price = item.find("span", class_="sm-offer-priceNum").text.strip()
    prices.append(price)

    # Variants (e.g., color, model, etc.)
    variant_tags = item.find_all("div", class_="variant-info")
    variant_info = [variant.text.strip() for variant in variant_tags]
    variants.append(variant_info)

    # Description
    description = item.find("div", class_="sm-offer-snapshot").text.strip()
    descriptions.append(description)

    # Reviews (if available)
    review_tag = item.find("span", class_="sm-offer-reviewCount")
    if review_tag:
        review = review_tag.text.strip()
    else:
        review = None
    reviews.append(review)

# Creating a DataFrame
df = pd.DataFrame({
    'Product': products,
    'Price': prices,
    'Variants': variants,
    'Description': descriptions,
    'Reviews': reviews
})

# Displaying the DataFrame
print(df)
