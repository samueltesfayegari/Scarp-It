import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def translate_text(text):
    translator = Translator()
    try:
        translated_text = translator.translate(text, src='auto', dest='en')
        if translated_text:
            return translated_text.text
        else:
            return ""
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

# def print_all_values(element):
#     # Print text value
#     text = element.get_text(strip=True)
#     if text:
#         translated_text = translate_text(text)
#         if translated_text:
#             print(translated_text)

#     # Print numeric value if present
#     if element.string and element.string.strip().isdigit():
#         print(element.string.strip())

#     # Recursively print values of child elements
#     for child in element.children:
#         if child.name:
#             print_all_values(child)

def scrape_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the parent container that holds all product listings
    products_container = soup.find_all("div", class_="")
    print(products_container)

    # Check if any products are found
    if not products_container:
        print("No products found.")
        return

    # Iterate through each product listing
    # for product in products_container:
    #     # Print only the text and numeric content of the product
    #     print_all_values(product)
    #     print("\n")

main_url = "https://www.1688.com/"
scrape_products(main_url)
