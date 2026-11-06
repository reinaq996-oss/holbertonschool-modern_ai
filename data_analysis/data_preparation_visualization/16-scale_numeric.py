#!/usr/bin/env python3
"""Standardize monthly and total customer charges."""
from sklearn import preprocessing


def scale_numeric(df):
    """Return a copy with MonthlyCharges and TotalCharges standardized."""
    scaled = df.copy()
    columns = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    scaled[columns] = scaler.fit_transform(scaled[columns])
    return scaled
