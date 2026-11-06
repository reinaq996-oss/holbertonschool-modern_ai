#!/usr/bin/env python3
"""Convert charge and senior citizen columns to their intended types."""
import pandas as pd


def convert_columns(df):
    """Convert TotalCharges and SeniorCitizen in place and return df."""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
