#!/usr/bin/env python3
"""Extract quotes from JSON-LD embedded in a webpage."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quote data from JSON-LD script blocks.

    Args:
        url (str): URL of the page to scrape.

    Returns:
        list: Dictionaries containing quote text, author, and tags.
    """
    quotes = []
    html = fetch_html(url)

    if not html:
        return quotes

    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all(
        'script',
        attrs={'type': 'application/ld+json'}
    )

    for script in scripts:
        if not script.string and not script.get_text(strip=True):
            continue

        try:
            data = json.loads(script.string or script.get_text())
        except (json.JSONDecodeError, TypeError):
            continue

        objects = data if isinstance(data, list) else [data]

        for obj in objects:
            if not isinstance(obj, dict):
                continue

            if obj.get('@type') != 'Quote':
                continue

            tags = obj.get('keywords', [])

            if isinstance(tags, str):
                tags = [
                    tag.strip()
                    for tag in tags.split(',')
                    if tag.strip()
                ]

            if not isinstance(tags, list):
                tags = []

            author = obj.get('author', {})
            if isinstance(author, dict):
                author = author.get('name', '')
            elif not isinstance(author, str):
                author = ''

            quotes.append({
                'text': obj.get('text'),
                'author': author,
                'tags': tags
            })

    return quotes
