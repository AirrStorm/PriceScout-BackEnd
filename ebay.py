# Import necessary libraries
from bs4 import BeautifulSoup  # Library for parsing HTML
import requests  # Library for making HTTP requests
import re  # Regular expression library for string manipulation

# Function to remove HTML comments
def remove_comments(soup): 
    if not isinstance(soup, str):  # Check if the input is not already a string
        soup = str(soup)  # Convert to string
    return re.sub(r'<!.*?->', '', soup)  # Use regular expression to remove HTML comments

# Scraping function for eBay
def scrape_ebay(search):
    result = []  # Initialize an empty list to store the scraped results
    search = search.replace(" ", "+")  # Replace spaces with "+" for the search URL
    search_URL = f"https://www.ebay.com/sch/i.html?_nkw={search}"  # Construct the search URL for eBay
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})  # Define headers to mimic a browser request

    # Send request to eBay search page
    request = requests.get(search_URL, headers=HEADERS).text  # Send GET request and retrieve the HTML content
    soup = BeautifulSoup(request, "html.parser")  # Parse the HTML content using BeautifulSoup

    # Loop through search results (indexes 2 to 6)
    for index in range(2, 7):
        try:
            try:
                # Find product information using specific HTML attributes
                product = soup.find("li", {"data-view": f"mi:1686|iid:{index}"}).prettify()  # Find the HTML element for the product
                product = BeautifulSoup(product, "html.parser")  # Parse the product HTML content

                # Extract product name
                name = product.find("span", {"role": "heading"}).prettify()  # Find the HTML element for the product name
                name = remove_comments(BeautifulSoup(name, "html.parser"))  # Remove HTML comments from the product name
                name = BeautifulSoup(name, "html.parser")  # Parse the product name HTML content

                # Extract product image URL
                image = product.find("img")  # Find the HTML element for the product image
                image = product.img["src"]  # Extract the "src" attribute containing the image URL

                # Extract product price
                price = product.find("span", {"class": "s-item__price"}).prettify()  # Find the HTML element for the product price
                price = remove_comments(BeautifulSoup(price, "html.parser"))  # Remove HTML comments from the product price
                price = BeautifulSoup(price, "html.parser")  # Parse the product price HTML content

                # Append product information to result list
                result.append({
                    "product_name": name.span.string.strip(),  # Extract and strip the text content of the product name
                    "product_price": price.span.string.strip(),  # Extract and strip the text content of the product price
                    "product_image": image  # Store the product image URL
                })

            except:
                pass  # Skip this iteration if extraction fails
        except Exception as err:
            pass  # Skip this iteration if an exception occurs

    return result  # Return the list of scraped results
