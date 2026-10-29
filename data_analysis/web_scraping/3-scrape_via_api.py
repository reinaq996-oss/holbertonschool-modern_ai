#!/usr/bin/env python3
"""Fetch quotes from the quotes.toscrape.com API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch all quotes using the site's paginated API.

    Args:
        base_url (str): Root URL of the website.

    Returns:
        list: Dictionaries containing quote text, author, and tags.
    """
    all_quotes = []
    page = 1

    while True:
        url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        response = fetch_html(url)

        if not response:
            break

        try:
            data = json.loads(response)
        except (json.JSONDecodeError, TypeError):
            break

        quotes = data.get('quotes', [])

        if not quotes:
            break

        for quote in quotes:
            all_quotes.append({
                'text': quote.get('text', ''),
                'author': quote.get('author', {}).get('name', ''),
                'tags': quote.get('tags', [])
            })

        if not data.get('has_next', False):
            break

        page += 1

    return all_quotes
