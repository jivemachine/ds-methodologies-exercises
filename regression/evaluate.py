import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from statsmodels.formula.api import ols

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt

# a function that plots residuals
def plot_residuals(df, y, y_hat):
    '''
    user inputs a dataframe, then Data or column name in data for the predictor variable.
    then Data or column name in data for the response variable. And 
    function will produce a scatter plot
    with a baseline
    '''
    sns.residplot(x=y, y=y_hat, data=df)


# function that produces a dataframe with information regarding regression errors
def regression_errors(y, yhat, df):
    '''
    input df.y value and df.yhat value to produce a 
    dataframe of regression errors and their values
    '''
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    import numpy as np
    import pandas as pd
    SSE = mean_squared_error(y, yhat)*len(df)
    ESS = sum((y - yhat.mean())**2)
    TSS = ESS + SSE
    MSE = mean_squared_error(y, yhat)
    RMSE = sqrt(mean_squared_error(y, yhat))
    ss = pd.DataFrame(np.array(['SSE','ESS','TSS', 'MSE', 'RMSE']), columns=['metric'])
    ss['model_values'] = np.array([SSE, ESS, TSS, MSE, RMSE])
    return ss



# function that computes SSE, MSE and RMSE for a baseline model and 
# returns the information in a dataframe
def baseline_mean_errors(y, yhat_baseline, df):
    '''
    input df.y value and df.baseline_yhat value to 
    produce a dataframe of baseline regression errors 
    and their values
    '''
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    import numpy as np
    import pandas as pd
    SSE_baseline = mean_squared_error(y, yhat_baseline)*len(df)
    MSE_baseline = mean_squared_error(y, yhat_baseline)
    RMSE_baseline = RMSE2_baseline = sqrt(mean_squared_error(y, yhat_baseline))
    baseline = pd.DataFrame(np.array(['SSE_baseline','MSE_baseline','RMSE_baseline']), columns=['metric'])
    baseline['model_error'] = np.array([SSE_baseline, MSE_baseline, RMSE_baseline])
    return baseline      


# function returns True if your model is more accurate than your baseline
def better_than_baseline(y, yhat, yhat_baseline, df):
    '''
    input df.y, df.yaht, df.yhat_baseline, df
    calculates SSE_baseline and SSE for the model
    then id the model's SSE is smaller than the baseline
    returns true
    '''
    SSE_baseline = mean_squared_error(y, yhat_baseline)*len(df)
    SSE_model = mean_squared_error(y, yhat)*len(df)
    return SSE_model < SSE_baseline


# takes a OLS model as input and returns the amount of variance in your mode and the f p-value
def model_significance(ols_model):
    '''
    takes an ols model as input and returns the r^2
    and the p-value
    '''
    r2 = model.rsquared
    p_value = model.f_pvalue
    df_model_sig = pd.DataFrame(np.array(['r^2', 'f p-value']), columns=['metric'])
    df_model_sig['value'] = np.array([r2, p_value])
    return df_model_sig
    
    