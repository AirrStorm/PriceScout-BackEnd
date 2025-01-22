from bs4 import BeautifulSoup
import requests
import re

# Function to remove HTML comments
def remove_comments(html_content):
    if isinstance(html_content, str):  # Ensure it's a string
        return re.sub(r'<!.*?-->', '', html_content)
    return html_content

# Scraping function for eBay
def scrape_ebay(search_term, num_results):
    results = []
    search_term = search_term.replace(" ", "+")
    search_url = f"https://www.ebay.com/sch/i.html?_nkw={search_term}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    # Send GET request
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error fetching eBay data: {e}")
        return results

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract product data
    for index in range(2, num_results + 2):
        try:
            product = soup.find("li", {"data-view": f"mi:1686|iid:{index}"})
            if not product:
                continue

            # Extract product name
            name_tag = product.find("span", {"role": "heading"})
            product_name = name_tag.get_text(strip=True) if name_tag else "N/A"

            # Extract product image
            img_tag = product.find("img")
            product_image = img_tag["src"] if img_tag and "src" in img_tag.attrs else "N/A"

            # Extract product price
            price_tag = product.find("span", {"class": "s-item__price"})
            product_price = price_tag.get_text(strip=True) if price_tag else "N/A"

            # Append result
            results.append({
                "product_name": product_name,
                "product_price": product_price,
                "product_image": product_image
            })

        except Exception as err:
            print(f"Error processing product {index}: {err}")
            continue

    return results
