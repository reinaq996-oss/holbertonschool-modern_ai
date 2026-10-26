
#!/usr/bin/env python3
"""Fetch HTML content from a URL."""

import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch HTML from a URL and return its content.

    Args:
        url: The URL to fetch.
        headers: Optional HTTP request headers.
        timeout: Request timeout in seconds.

    Returns:
        The HTML content as a string.

    Raises:
        requests.RequestException: If the request fails.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
