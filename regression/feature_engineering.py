import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE


# feature selecting function using K-best
def select_kbest(predictors, target, features):
    '''
    function that inputs predictors(X_train), target(y_train), and the # of features desired and uses 
    KBest from SKlearn to select what features to use
    '''
    kbest = SelectKBest(f_regression, features)
    kbest.fit(predictors, target)
    return predictors.columns[kbest.get_support()]



# feature selecting function using recursive feature elimination 
def select_rfe(predictors, target, features):
    '''
    function that inputs predictors(X_train), target(y_train), # of features desired and uses
    recursive feature elimination from SKlearn to select what features to use
    '''
    lm = LinearRegression()
    rfe = RFE(lm, features)
    # Transforming data using RFE
    rfe.fit(predictors, target)
    return predictors.columns[rfe.support_]
