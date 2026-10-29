#!/usr/bin/env python3
"""Scrape quotes from the first page of Quotes to Scrape."""

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape quotes, authors, and tags from a webpage.

    Args:
        url: The URL of the quotes page.

    Returns:
        A list of dictionaries containing quote text, author, and tags.
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    quotes = []

    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text(strip=True)
        author = quote.select_one('small.author').get_text(strip=True)
        tags = [
            tag.get_text(strip=True)
            for tag in quote.select('div.tags a.tag')
        ]

        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes
