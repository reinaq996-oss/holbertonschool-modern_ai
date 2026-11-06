#!/usr/bin/env python3
"""Create service counts and tenure groups for customer analysis."""
import pandas as pd


def create_features(df):
    """Return a copy with engineered features replacing their sources."""
    services = [
        'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    result = df.copy()
    result['NumServices'] = (
        result[services].eq('Yes').sum(axis=1)
        + result['InternetService'].isin(['DSL', 'Fiber optic']).astype(int)
    )
    result['TenureGroup'] = pd.cut(
        result['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'],
        right=True,
        include_lowest=False
    )
    return result.drop(columns=services + ['InternetService', 'tenure'])
