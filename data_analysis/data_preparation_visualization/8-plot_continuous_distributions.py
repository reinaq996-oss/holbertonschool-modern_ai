#!/usr/bin/env python3
"""Plot histograms, density estimates, and boxplots for numeric features."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Display and save distributions for the selected numeric columns."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include='number').columns.tolist()

    n_cols = len(columns_to_plot)
    if n_cols == 0:
        return None

    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))
    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, column in enumerate(columns_to_plot):
        data = df[column].dropna()
        if not data.empty:
            axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                            edgecolor='black')
            if len(data) > 1 and data.nunique() > 1:
                kde = stats.gaussian_kde(data)
                x = np.linspace(data.min(), data.max(), 200)
                axes[i, 0].plot(x, kde(x), color='red', linestyle='--')
            axes[i, 1].boxplot(data, vert=False)
        axes[i, 0].set_title(f"{column} Histogram + KDE")
        axes[i, 1].set_title(f"{column} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
