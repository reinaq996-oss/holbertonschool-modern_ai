#!/usr/bin/env python3
"""Handle missing total charges using a selected cleaning strategy."""


def clean_total_charges(df, method='drop'):
    """Return a cleaned copy of df without changing the original.

    Strategies are 'drop', 'median', and 'impute' (monthly charges times
    tenure). Unsupported strategies raise ValueError.
    """
    cleaned = df.copy()
    if method == 'drop':
        cleaned = cleaned.dropna(subset=['TotalCharges'])
    elif method == 'median':
        cleaned['TotalCharges'] = cleaned['TotalCharges'].fillna(
            cleaned['TotalCharges'].median()
        )
    elif method == 'impute':
        cleaned['TotalCharges'] = cleaned['TotalCharges'].fillna(
            cleaned['MonthlyCharges'] * cleaned['tenure']
        )
    else:
        raise ValueError("method must be 'drop', 'median', or 'impute'")
    return cleaned
