#!/usr/bin/env python3
"""Scrape quotes from all pages of quotes.toscrape.com."""

from bs4 import BeautifulSoup
import time
from urllib import parse

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape quotes from a page and follow Next links until the end.

    Args:
        base_url (str): URL of the first page to scrape.

    Returns:
        list: A list of dictionaries containing quote text, author, and tags.
    """
    all_quotes = []
    current_url = base_url
    visited_urls = set()

    while current_url and current_url not in visited_urls:
        visited_urls.add(current_url)

        quotes = scrape_basic(current_url)
        if quotes:
            all_quotes.extend(quotes)

        html = fetch_html(current_url)
        if not html:
            break

        soup = BeautifulSoup(html, 'html.parser')
        next_link = soup.select_one('li.next a')

        if next_link and next_link.get('href'):
            current_url = parse.urljoin(
                current_url,
                next_link['href']
            )
            time.sleep(1)
        else:
            current_url = None

    return all_quotes
