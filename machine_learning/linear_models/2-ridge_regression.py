#!/usr/bin/env python3
"""Create a Ridge regression model."""

from sklearn import linear_model


def ridge_regression(random_state):
    """Return an untrained Ridge model with the given random seed."""
    return linear_model.Ridge(random_state=random_state)
