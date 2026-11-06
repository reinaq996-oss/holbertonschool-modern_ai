#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Return a DataFrame containing the first occurrence of each row."""
    return df.drop_duplicates()
