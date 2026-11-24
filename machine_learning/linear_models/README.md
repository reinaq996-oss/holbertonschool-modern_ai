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

## Understanding the models and metrics

Ordinary least squares minimizes the sum of squared prediction errors. Ridge
adds an L2 penalty that shrinks coefficients and can stabilize models when
features are strongly correlated. Lasso adds an L1 penalty that can set some
coefficients to zero, providing feature selection.

The three model factory functions return untrained estimators with default
Scikit-learn settings. Ridge and Lasso receive the supplied `random_state`.

| Metric | Interpretation |
| --- | --- |
| MSE | Average squared error; smaller is better. |
| RMSE | Square root of MSE, expressed in the target's units. |
| MAE | Average absolute error, expressed in the target's units. |
| R-squared | Explained variance relative to a mean predictor; 1 is perfect, and values can be negative. |

## Usage example

Run this example from `machine_learning/linear_models` so Python can find the
numbered modules:

```python
import numpy as np
from sklearn.model_selection import train_test_split

ridge_regression = __import__('2-ridge_regression').ridge_regression
metrics = __import__('1-regression_evaluation_metrics')
get_shap = __import__('4-shap').get_shap_explainer_and_values

rng = np.random.default_rng(42)
X = rng.normal(size=(100, 3))
y = X @ np.array([4.0, 0.0, 3.0]) + rng.normal(size=100)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = ridge_regression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse, rmse, mae, r2 = metrics.evaluation_metrics_for_regression(y_test, y_pred)
print(f'MSE: {mse:.4f}, RMSE: {rmse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}')

explainer, shap_values = get_shap(model, X_train, X_test)
print('SHAP values shape:', shap_values.values.shape)
```

## SHAP explanations

`get_shap_explainer_and_values` initializes `shap.Explainer(model, X_train)`
and calls the explainer on `X_test`. It returns the explainer and a SHAP
`Explanation` object that can be passed to plotting functions:

```python
import shap

shap.plots.bar(shap_values)
shap.plots.beeswarm(shap_values)
```

A positive SHAP value increases the prediction relative to the baseline; a
negative value decreases it. For these regression models, the baseline plus
the feature contributions reconstructs each prediction. SHAP's default
background masker may sample large training datasets.
