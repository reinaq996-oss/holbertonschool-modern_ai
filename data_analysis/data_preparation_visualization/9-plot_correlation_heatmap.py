#!/usr/bin/env python3
"""Visualize pairwise correlations between numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Display an annotated correlation heatmap for numeric columns."""
    plt.figure(figsize=(6, 5))
    correlations = df.select_dtypes(include='number').corr()
    sns.heatmap(correlations, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.show()
