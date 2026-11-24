#!/usr/bin/env python3
"""Compute common regression evaluation metrics."""

from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """Return MSE, RMSE, MAE, and R-squared for the predictions."""
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    return mse, rmse, mae, r2
