#!/usr/bin/env python3
"""Module that plots the churn class distribution of a dataset."""
import matplotlib.pyplot as plt




def plot_churn_distribution(df):
    """Plot the distribution of the Churn column as a bar plot.

    The bar for 'No' is drawn in skyblue and the bar for 'Yes' in
    salmon, regardless of the order of the value counts.

    Args:
        df (pandas.DataFrame): DataFrame containing a 'Churn' column
            with the values 'No' and 'Yes'.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    colors = ['skyblue' if label == 'No' else 'salmon'
              for label in counts.index]

    plt.bar(counts.index, counts.values, color=colors)
    plt.show()
