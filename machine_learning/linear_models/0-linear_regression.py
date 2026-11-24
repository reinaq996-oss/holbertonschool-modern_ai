#!/usr/bin/env python3
"""Create an ordinary least squares linear regression model."""

from sklearn import linear_model


def Linear_Regression():
    """Return an untrained LinearRegression instance with default settings."""
    return linear_model.LinearRegression()
