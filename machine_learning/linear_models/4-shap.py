#!/usr/bin/env python3
"""Generate SHAP explanations for a trained regression model."""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Return the explainer and test explanations using training background."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
