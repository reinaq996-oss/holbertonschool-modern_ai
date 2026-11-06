#!/usr/bin/env python3
"""Compare numeric feature distributions between churn groups."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Display histograms of a numeric column grouped by churn status."""
    no_churn = df.loc[df['Churn'] == 'No', col].dropna()
    churn = df.loc[df['Churn'] == 'Yes', col].dropna()

    plt.figure(figsize=(12, 8))
    plt.hist([no_churn, churn], bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
