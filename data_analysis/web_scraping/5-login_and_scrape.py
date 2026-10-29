
#!/usr/bin/env python3
"""Log in to a website and scrape its quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and retrieve quotes using an authenticated session.

    Args:
        login_url (str): URL of the login page.
        user (str): Username for authentication.
        pwd (str): Password for authentication.

    Returns:
        list: Dictionaries containing quote text, author, and tags.
    """
    quotes = []

    with requests.Session() as session:
        response = session.get(login_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_input = soup.find('input', attrs={'name': 'csrf_token'})

        if csrf_input is None:
            return quotes

        csrf_token = csrf_input.get('value', '')

        payload = {
            'username': user,
            'password': pwd,
            'csrf_token': csrf_token
        }

        response = session.post(
            login_url,
            data=payload,
            timeout=10
        )
        response.raise_for_status()

        quotes_url = 'https://quotes.toscrape.com/'
        response = session.get(quotes_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.find_all('div', class_='quote'):
            text_element = quote.find(
                'span',
                class_='text'
            )
            author_element = quote.find(
                'small',
                class_='author'
            )
            tag_elements = quote.find_all(
                'a',
                class_='tag'
            )

            quotes.append({
                'text': text_element.get_text(strip=True)
                if text_element else '',
                'author': author_element.get_text(strip=True)
                if author_element else '',
                'tags': [
                    tag.get_text(strip=True)
                    for tag in tag_elements
                ]
            })

    return quotes
