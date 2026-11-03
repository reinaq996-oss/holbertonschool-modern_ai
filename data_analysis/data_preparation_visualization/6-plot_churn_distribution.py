#!/usr/bin/env python3
"""Visualizes the churn class distribution as a bar plot."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Plot a bar chart of Churn value counts (No skyblue, Yes salmon)."""
    churn_counts = df["Churn"].value_counts()
    colors = ["skyblue" if label == "No" else "salmon"
              for label in churn_counts.index]

    plt.figure(figsize=(12, 8))
    plt.bar(churn_counts.index, churn_counts.values, color=colors)
    plt.title("Churn Distribution")
    plt.ylabel("Count")
    plt.show()
