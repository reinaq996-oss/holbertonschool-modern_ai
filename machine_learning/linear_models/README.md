# Linear Models

Scikit-learn regression models, evaluation metrics, and SHAP explanations.

| File | Function | Description |
| --- | --- | --- |
| `0-linear_regression.py` | `Linear_Regression()` | Return an untrained ordinary least squares model. |
| `1-regression_evaluation_metrics.py` | `evaluation_metrics_for_regression(y_true, y_pred)` | Return `(mse, rmse, mae, r2)`. |
| `2-ridge_regression.py` | `ridge_regression(random_state)` | Return an untrained Ridge model with L2 regularization. |
| `3-Lasso_regression.py` | `lasso_regression(random_state)` | Return an untrained Lasso model with L1 regularization. |
| `4-shap.py` | `get_shap_explainer_and_values(model, X_train, X_test)` | Use training data as the SHAP background and return the explainer and test explanations. |

## Requirements

Install NumPy, Scikit-learn, and SHAP in your Python environment:

```sh
python -m pip install numpy scikit-learn shap
```

Train each model with `fit(X_train, y_train)` before predicting or computing
SHAP explanations. Pass predictions and true targets to the evaluation function.

## Validation

The functions were checked against the supplied regression examples. Checks
also confirmed that model factories return untrained models, Lasso selects six
features in the supplied example, and SHAP contributions plus base values match
model predictions.
