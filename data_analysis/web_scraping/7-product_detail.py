#!/usr/bin/env python3
"""Scrape details from a single product page."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_product_detail(url, delay=2.0):
    """Extract details of a single product.

    Args:
        url (str): URL of the product detail page.
        delay (float): Number of seconds to wait after loading.

    Returns:
        dict: Product title, price, description, and rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element(
            By.CSS_SELECTOR,
            '.caption'
        )
        headings = caption.find_elements(By.TAG_NAME, 'h4')

        title = headings[1].text.strip()

        price = driver.find_element(
            By.CSS_SELECTOR,
            'h4.price'
        ).text.strip()

        description = driver.find_element(
            By.CSS_SELECTOR,
            'p.description'
        ).text.strip()

        stars = driver.find_elements(
            By.CSS_SELECTOR,
            '.ratings p.ws-icon.ws-icon-star'
        )

        return {
            'title': title,
            'price': price,
            'description': description,
            'rating': len(stars)
        }

    finally:
        driver.quit()
