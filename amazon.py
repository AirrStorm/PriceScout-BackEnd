# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to scrape product information from Amazon
def scrape_amazon(search):
    result = []

    # Prepare the search query and URL
    search = search.replace(" ", "+")
    Search_URL = f"https://www.amazon.com/s?k={search}"

    # Set user agent and language headers for the request
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

    # Send request to Amazon search page and retrieve HTML content
    request = requests.get(Search_URL, headers=HEADERS).text
    soup = BeautifulSoup(request, "html.parser")

    # Loop through search results (from index 2 to 6)
    for index in range(2, 7):
        product_price = None  # Initialize product_price as None
        try:
            # Try to find product information using specific attributes
            product = soup.find("div", {"cel_widget_id": f"MAIN-SEARCH_RESULTS-{index}"}).prettify()
            product = BeautifulSoup(product, "html.parser")

            product_name = product.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).prettify()
            product_name = BeautifulSoup(product_name, "html.parser")

            image = product.find("img")
            image = product.img["src"]

            product_price = product.find("span", {"class": "a-offscreen"})  # Assign BeautifulSoup object directly
        except:
            try:
                # Try alternative method to find product information
                product = soup.find("div", {"class": f"s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_{index}"}).prettify()
                product = BeautifulSoup(product, "html.parser")

                product_name = product.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).prettify()
                product_name = BeautifulSoup(product_name, "html.parser")

                image = product.find("img")
                image = image.get('src')

                product_price = product.find("span", {"class": "a-offscreen"})  # Assign BeautifulSoup object directly
            except:
                pass

        # Check if product_price is None and handle accordingly
        if product_price is None :
            product_price = "N/A"  # If product price not found, set it to "N/A"
        else:
            product_price = product_price.string.strip()  # Extract the product price

        # Append the product information to the result list
        result.append({
            "endpoint": "amazon",
            # "product_name": product_name.span.string.strip(),
            "product_price": product_price,
            "product_image": image
        })
    
    return result
