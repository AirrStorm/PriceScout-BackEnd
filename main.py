# Import necessary libraries
import json
# Import scraping functions from respective modules
from amazon import scrape_amazon
from jumia import scrape_jumia
from ebay import scrape_ebay

# Prompt user to enter a search query
search = input("Enter a search: ")
amount = input("Enter the amount of products to scrape: ")

# Call scraping functions for Amazon, Jumia, and eBay
result = {
    # "amazon": scrape_amazon(search),
    "jumia": scrape_jumia(search),
    "ebay": scrape_ebay(search, int(amount))
}

# Print the result in a formatted JSON string
print(json.dumps(result, indent=4))
