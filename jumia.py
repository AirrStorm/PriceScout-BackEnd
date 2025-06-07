# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to scrape product information from Jumia
def scrape_jumia(search):
    result= []

    # Prepare the search query and URL
    search = search.replace(" ", "+")
    search_URL = f"https://www.jumia.com.gh/catalog/?q={search}"


    # Set user agent and language headers for the request
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

    # Send request to Jumia search page and retrieve HTML content
    request = requests.get(search_URL, headers=HEADERS).text
    soup = BeautifulSoup(request, "html.parser")

    # Loop through the first 5 search results
    for index in range(1, 6):
        try:
            # Find the product information for each search result
            product = soup.find("a", {"data-gtm-position": {index}}).prettify()
            product = BeautifulSoup(product, "html.parser")

            # Extract the product name
            name = product.find("h3", ["class", "name"]).prettify()
            name = BeautifulSoup(name, "html.parser")

            # Extract the product image URL
            image = product.find("img")
            image = product.img["data-src"]

            # Extract the product price
            price = product.find("div", {"class": "prc"}).prettify()
            price = BeautifulSoup(price, "html.parser")

            # Append the product information to the result list
            result.append({
                "product_name": name.h3.string.strip(),
                "product_price": price.div.string.strip(),
                "product_image": image
            })

        except Exception as err:
            pass # Skip this iteration if an exception occurs

    return result # Return the list of scraped results
