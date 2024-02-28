# Web Scraping Scripts

## Introduction

This repository contains Python scripts for scraping product information from various e-commerce websites. The scripts utilize web scraping techniques to extract data such as product names, prices, and image URLs from Amazon, Jumia, and eBay.

## Scripts

### 1. Amazon Scraper (`amazon.py`)

- The `amazon.py` script is designed to scrape product information from Amazon.
- It uses BeautifulSoup and requests libraries to parse HTML content and make HTTP requests.
- The `scrape_amazon` function accepts a search query as input and returns a list of dictionaries containing product details.

### 2. Jumia Scraper (`jumia.py`)

- The `jumia.py` script scrapes product information from the Jumia website.
- Similar to the Amazon scraper, it employs BeautifulSoup and requests libraries for web scraping.
- The `scrape_jumia` function takes a search query as input and returns a list of dictionaries containing product details.

### 3. eBay Scraper (`ebay.py`)

- The `ebay.py` script is responsible for scraping product information from eBay.
- It follows a similar structure as the Amazon and Jumia scrapers, using BeautifulSoup and requests libraries.
- The `scrape_ebay` function accepts a search query as input and returns a list of dictionaries containing product details.

### 4. Main Script (`main.py`)

- The `main.py` script orchestrates the scraping process by calling the scraping functions from the Amazon, Jumia, and eBay scripts.
- It prompts the user to input a search query and then invokes the scraping functions with the provided query.
- Finally, it aggregates the results from all three websites and prints them in a formatted JSON string.

## Usage

1. Ensure Python is installed on your system.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Run the `main.py` script. It will prompt you to input a search query.
4. After providing the search query, the script will scrape product information from Amazon, Jumia, and eBay, and display the results in JSON format.

## Disclaimer

- These scripts are provided for educational purposes and demonstrate basic web scraping techniques.
- Before scraping any website, ensure compliance with the website's terms of service and legal requirements.
- Web scraping may be prohibited or restricted by some websites. Use these scripts responsibly and ethically.
