# pytruncreg Overview
The `pytruncreg` package developed by [Harvard University's CausaLab](https://causalab.sph.harvard.edu/) is designed to estimate one-way truncated gaussian regression models. The `truncreg` function requires `formula`, `data`, a truncation `point` and `direction` of truncation. This python package is a translation of the original `truncreg` R package [CRAN](https://cran.r-project.org/web/packages/truncreg/index.html) by Yves Croissant and Achim Zeileis.

## Parameters
- **formula** (str): String describing the model to be fitted in format `y ~ x_1 + x_2 + ... x_n`
- **data** (DataFrame): The dataset containing the variables specified in the formula
- **point** (float): The point of truncation in `y`
- **direction** (str): Specifies the direction of truncation, taking values `"left"` or `"right"`
- **scaled** (bool, optional): Default is `False`. When set to `True` the model will use a scaled version of the dependent variable
- **iterlim** (int, optional): Default is 50. The maximum iterations for the optimization algorithm.

## Returns
- `OptimizeResult`: an object containing the results of the results of the optimization algorithm
- `SE` an array containing the standard errors for intercept and coefficients
- `vcov` the hessian (variance-covariance matrix) from the optimization process

## Description
The `truncreg` function based on the original `truncreg` R package [CRAN](https://cran.r-project.org/web/packages/truncreg/index.html) by Yves Croissant and Achim Zeileis, performs maximum likelihood estimation of a truncated gaussian regression model. The function supports both left and right truncation and will extract variables inside of `formula` from the provided `data` then constructs the model matrix by supplying an intercept and fits the truncated regression model using the L-BFGS-B optimization algorithm. Internally, the function calculates the log-likelihood, gradient, and Hessian matrix for the optimization process. The initial values for beta coefficients are estimated using ordinary least squares.\\
In the case of overflow, `truncreg` will attempt to handle potential overflow issues in calculating the Mills ratio and log-likelihood. If `scaled=True`, the dependent variable is scaled before estimation.

## Example Usage
```python
import pandas as pd
import numpy as np
from pytruncreg import truncreg

np.random.seed(42)
data = pd.DataFrame({
    'y': np.random.normal(0, 1, 1000),
    'x1': np.random.normal(1, 3, 1000),
    'x2': np.random.normal(10, 3, 1000)
})

result = truncreg(formula='y~x1+x2', data=data, point=-4, direction='left')
print(result)
```

# Dependencies
- numpy
- scipy.stats
- scipy.optimize
- re
