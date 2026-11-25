#!/usr/bin/env python3
"""Create a logistic regression classifier."""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Return an untrained logistic classifier with the given random seed."""
    return linear_model.LogisticRegression(random_state=random_state)
