#!/usr/bin/env python3
"""Compare numeric feature means between churn groups with Welch's test."""
from scipy import stats


def ttest_numeric(df):
    """Return two-sided Welch's t-test p-values for numeric features."""
    p_values = {}
    for feature in df.select_dtypes(include='number').columns:
        if feature == 'Churn':
            continue
        churn = df.loc[df['Churn'] == 'Yes', feature].dropna()
        no_churn = df.loc[df['Churn'] == 'No', feature].dropna()
        p_values[feature] = stats.ttest_ind(
            churn, no_churn, equal_var=False
        ).pvalue
    return p_values
