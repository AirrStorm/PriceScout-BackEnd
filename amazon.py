# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to scrape product information from Amazon
def scrape_amazon(search, amount):
    result = []

    # Prepare the search query and URL
    search = search.replace(" ", "+")
    Search_URL = f"https://www.amazon.com/s?k={search}"

    # Set user agent and language headers for the request
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0', 'Accept-Language': 'en-US, en;q=0.5'}

    # Send request to Amazon search page and retrieve HTML content
    request = requests.get(Search_URL, headers=HEADERS).text
    soup = BeautifulSoup(request, "html.parser")

    product_count = 0
    # Loop through search results (from index 2 to 6)
    for index in range(2, amount + 2):
        product_price = None  # Initialize product_price as None
        product_name = None  # Initialize product_name as None
        
        try:
            # Try to find product information using specific attributes
            product = soup.find("div", {"class": f"widgetId=search-results_{index}"})
            product = BeautifulSoup(str(product), "html.parser")

            product_name = product.find("h2", {"class": "a-size-medium a-spacing-none a-color-base a-text-normal"}).prettify()
            product_name = BeautifulSoup(product_name, "html.parser")
            product_name = product_name.span.string.strip()
            # print(f"{product_name}\n \n")

            product_link = product.find("a", {"class": "s-line-clamp-2"})
            if product_link:
                # Extract the href attribute which contains the link
                product_href = product_link.get("href")
                product_href = f"https://www.amazon.com/{product_href}"

                # print(f"Product Link: https://www.amazon.com/{product_href}")
            else:
                print("Product link not found")
            image = product.find("img")
            image = product.img["src"]

            product_price = product.find("span", {"class": "a-offscreen"})
            if product_price:
                product_price = product_price.get_text(strip=True)

            result.append({
                "product_name": product_name,
                "product_price": product_price,
                "product_image": image,
                "product_link": product_href
        })

        except Exception as e:
            print(f"Error processing product at index {index}: {e}")
            continue  # Skip to the next product in case of error

    return result


            # try:
            #     # Try alternative method to find product information
            #     product = soup.find("div", {"class": f"s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_{index}"}).prettify()
            #     product = BeautifulSoup(product, "html.parser")

            #     product_name = product.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).prettify()
            #     product_name = BeautifulSoup(product_name, "html.parser")

            #     image = product.find("img")
            #     image = image.get('src')

            #     product_price = product.find("span", {"class": "a-offscreen"})  # Assign BeautifulSoup object directly
            # except:
            #     pass

        # Check if product_price is None and handle accordingly
        # if product_price is None:
        #     product_price = "N/A"  # If product price not found, set it to "N/A"
        # else:
        #     product_price = product_price.string.strip()  # Extract the product price

        # Only append to result if product_name was successfully assigned
    #     if product_name:
    #     result.append({
    #         "endpoint": "amazon",
    #         "product_name": product_name,
    #         "product_price": product_price,
    #         "product_image": image,
    #         "product": product
    #     })
    
    # return result
