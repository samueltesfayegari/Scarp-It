import requests
from bs4 import BeautifulSoup

def scrape_products(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the parent container that holds all product listings
    products_container = soup.find_all("div", class_="")
    
    # Check if any products are found
    if not products_container:
        print("No products found.")
        return
    
    # Create an HTML file and write the product information into it
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Scraped Products</title></head><body>")
        
        # Iterate through each product listing
        for product in products_container:
            # Write the product information to the HTML file
            f.write(str(product))
        
        f.write("</body></html>")
    
    print(f"Product information saved to '{output_file}'")

main_url = "https://www.1688.com/"
output_file = "scraped_products.html"
scrape_products(main_url, output_file)
