#!/usr/bin/env python3
"""Scroll through an infinite-scroll page and scrape products.

This module uses Selenium in headless Chrome to scroll a JS-rendered
page until no more content loads, then extracts the unique products.
"""
import time
from selenium import webdriver


def _wait_for_growth(driver, last_height, scroll_pause):
    """Wait until the page grows or the pause expires.

    Args:
        driver: Selenium WebDriver instance.
        last_height (int): Page height before the last scroll.
        scroll_pause (float): Maximum seconds to wait.

    Returns:
        int: The new page height (equal to last_height on timeout).
    """
    deadline = time.time() + scroll_pause
    height = last_height
    while time.time() < deadline:
        time.sleep(0.1)
        height = driver.execute_script(
            'return document.body.scrollHeight'
        )
        if height > last_height:
            return height
    return height


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to load all products and extract unique product details.

    Opens the page in headless Chrome (1920x1080, no sandbox), scrolls
    to the bottom repeatedly, waiting up to ``scroll_pause`` seconds
    each time, until the page height stops increasing. Duplicate
    products are skipped by tracking (title, price) pairs.

    Args:
        url (str): URL of the infinite-scroll product page.
        scroll_pause (float): Seconds to wait after each scroll.

    Returns:
        list: Unique product dictionaries, each containing:
            - "title" (str): title attribute of the a.title link
            - "price" (str): text of the h4.price element
            - "description" (str): text of the p.description element
            - "rating" (int): number of star icons inside .ratings
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()
    try:
        driver.get(url)
        last_height = driver.execute_script(
            'return document.body.scrollHeight'
        )
        while True:
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);'
            )
            new_height = _wait_for_growth(
                driver, last_height, scroll_pause
            )
            if new_height <= last_height:
                break
            last_height = new_height
        cards = driver.find_elements('css selector', 'div.thumbnail')
        for card in cards:
            link = card.find_element('css selector', 'a.title')
            price = card.find_element('css selector', 'h4.price')
            description = card.find_element(
                'css selector', 'p.description'
            )
            stars = card.find_elements(
                'css selector', '.ratings .ws-icon-star'
            )
            title_text = link.get_attribute('title')
            price_text = price.text.strip()
            key = (title_text, price_text)
            if key in seen:
                continue
            seen.add(key)
            products.append({
                'title': title_text,
                'price': price_text,
                'description': description.text.strip(),
                'rating': len(stars)
            })
    finally:
        driver.quit()
    return products
