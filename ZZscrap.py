from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def print_all_values(element):
    # Print text value
    text = element.text.strip()
    if text:
        translated_text = translate_text(text)
        if translated_text:
            print(translated_text)

    # Print numeric value if present
    if element.text.strip().isdigit():
        print(element.text.strip())

    # Recursively print values of child elements
    for child in element.find_elements(By.XPATH, ".//*"):
        print_all_values(child)

def scrape_products(url):
    # Specify the path to the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get(url)

    try:
        # Find the parent container that holds all product listings
        products_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "changhuo-offer-list"))
        )

        print("Number of products found:", products_container)

        # Iterate through each product listing
        # for product in products_container:
        #     # Print only the text and numeric content of the product
        #     print_all_values(product)
        #     print("\n")
    except Exception as e:
        print("Error occurred while scraping products:", e)

    # Quit the WebDriver
    driver.quit()

# Start scraping from the main page
main_url = "https://www.1688.com/"
scrape_products(main_url)
