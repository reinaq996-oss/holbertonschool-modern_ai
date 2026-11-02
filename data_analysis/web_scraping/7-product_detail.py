#!/usr/bin/env python3
"""Scrape details from a single product page.

This module uses Selenium in headless Chrome to open the detail
page of one product and extract its title, price, description and
rating.
"""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Extract the details of a single product.

    Opens the page in headless Chrome (1920x1080, no sandbox), waits
    for ``delay`` seconds, and reads the product information.

    Args:
        url (str): URL of the product detail page.
        delay (float): Number of seconds to wait after loading.

    Returns:
        dict: Product information containing:
            - "title" (str): text of the second h4 inside .caption
            - "price" (str): text of the first h4.price element
            - "description" (str): text of the p.description element
            - "rating" (int): number of star icons inside .ratings
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)
        headings = driver.find_elements('css selector', '.caption h4')
        title = headings[1].text.strip()
        price = driver.find_element('css selector', 'h4.price')
        description = driver.find_element(
            'css selector', 'p.description'
        )
        stars = driver.find_elements(
            'css selector', '.ratings .ws-icon-star'
        )
        return {
            'title': title,
            'price': price.text.strip(),
            'description': description.text.strip(),
            'rating': len(stars)
        }
    finally:
        driver.quit()
