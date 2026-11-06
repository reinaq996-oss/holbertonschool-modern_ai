#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot missing entries by row index and explicitly labeled column."""
    plt.figure(figsize=(12, 8))

    rows, columns = np.where(df.isna())
    plt.scatter(df.index.to_numpy()[rows], columns, marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.title("Missingness Plot")

    plt.tight_layout()
    plt.show()
