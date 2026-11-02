#!/usr/bin/env python3
"""Scrape products from a static e-commerce category page.

This module uses Selenium in headless Chrome to open a product
category page and extract the title, price, description and rating
of every product listed on it.
"""
import time
from selenium import webdriver


def scrape_products(url):
    """Scrape product details from a category page.

    Opens the page in headless Chrome (1920x1080, no sandbox), waits
    briefly for it to load, and reads the details of each product card.

    Args:
        url (str): URL of the product category page.

    Returns:
        list: Dictionaries, one per product, each containing:
            - "title" (str): product name, from the link's title attribute
            - "price" (str): text of the h4.price element
            - "description" (str): text of the p.description element
            - "rating" (int): number of stars, from the data-rating
              attribute of the paragraph under .ratings
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    products = []
    try:
        driver.get(url)
        time.sleep(2)
        cards = driver.find_elements('css selector', '.thumbnail')
        for card in cards:
            title = card.find_element('css selector', 'a.title')
            price = card.find_element('css selector', 'h4.price')
            description = card.find_element(
                'css selector', 'p.description'
            )
            rating = card.find_element(
                'css selector', '.ratings p[data-rating]'
            )
            products.append({
                'title': title.get_attribute('title'),
                'price': price.text.strip(),
                'description': description.text.strip(),
                'rating': int(rating.get_attribute('data-rating'))
            })
    finally:
        driver.quit()
    return products


scrape_products_list = scrape_products
