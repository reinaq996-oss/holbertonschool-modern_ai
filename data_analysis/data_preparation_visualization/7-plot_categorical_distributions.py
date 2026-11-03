#!/usr/bin/env python3
""" Module that plots categorical feature distributions."""

import math
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plot the distributions of categorical features.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.
        columns_to_plot (list): List of categorical columns to plot.
            Defaults to all object columns except 'Churn'.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include='object'
        ).columns.drop('Churn', errors='ignore').tolist()

    else:
        columns_to_plot = columns_to_plot

    if not columns_to_plot:
        return None

    n_cols = 3
    n_rows = math.ceil(len(columns_to_plot) / n_cols)

    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(15, 5 * n_rows)
    )

    axes = axes.flatten()

    for i, column in enumerate(columns_to_plot):
        counts = df[column].value_counts()

        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(column)
        axes[i].tick_params(axis='x', labelrotation=45)

    for i in range(len(columns_to_plot), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()

    return None
