# Holberton School - Modern AI

Practical exercises in data analysis and machine learning using Python.
The repository includes data preparation, visualization, regression models,
and model interpretation with SHAP.

## Project structure

- `data_analysis/`: exercises for preparing, exploring, and visualizing data.
- `machine_learning/linear_models/`: linear regression, Ridge, Lasso,
  regression evaluation metrics, and SHAP explanations.

See the [Linear Models guide](machine_learning/linear_models/README.md) for
function descriptions, installation instructions, and a complete usage example.

## Setup

Use a Python virtual environment and install the packages needed for the
regression exercises:

```sh
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```sh
source .venv/bin/activate
```

Then install the dependencies:

```sh
python -m pip install numpy scikit-learn shap matplotlib
```

## Learning goals

- Prepare data for analysis and model training.
- Compare ordinary least squares with L1 and L2 regularization.
- Evaluate predictions using MSE, RMSE, MAE, and R-squared.
- Explain feature contributions using SHAP values.
