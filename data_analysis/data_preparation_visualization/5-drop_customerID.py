#!/usr/bin/env python3
"""Remove the customer identifier column from a DataFrame."""


def drop_customerID(df):
    """Return a DataFrame with the customerID column removed."""
    return df.drop(columns=['customerID'])
