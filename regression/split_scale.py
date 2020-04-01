import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.preprocessing

#split_my_data(X, y, train_pct)
def split_my_data(X, y, train_pct=.08):
    return train_test_split(X, y, test_size=train_pct, random_state=830)

#standard_scaler()
def standard_scaler(train_data, test_data):
    '''
    takes in test data and train data and fits them both
    '''
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(train_data)
    test_scaled = pd.DataFrame(scaler.transform(test_data), columns=test_data.columns, index=test_data.index)
    train_scaled = pd.DataFrame(scaler.transform(train_data), columns=train_data.columns, index=train_data.index)
    return scaler, train_scaled, test_scaled



#scale_inverse()
def scale_inverse(scaler, train_scaled, test_scaled):
    train = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns.values).set_index([train_scaled.index.values])
    test = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns.values).set_index([test_scaled.index.values])
    return scaler, train, test


#uniform_scaler()
def uniform_scaler(train_data, test_data):
    '''
    takes in test data and train data and fits them both
    '''
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True)
    scaler.fit(train_data)
    test_scaled = pd.DataFrame(scaler.transform(test_data), columns=test_data.columns, index=test_data.index)
    train_scaled = pd.DataFrame(scaler.transform(train_data), columns=train_data.columns, index=train_data.index)
    return scaler, train_scaled, test_scaled


#gaussian_scaler()
def gaussian_scaler(train_data, test_data, method='yeo-johnson'):
    scaler = PowerTransformer(method, standardize=False, copy=True)
    scaler.fit(train_data)
    test_scaled = pd.DataFrame(scaler.transform(test_data), columns=test_data.columns, index=test_data.index)
    train_scaled = pd.DataFrame(scaler.transform(train_data), columns=train_data.columns, index=train_data.index)
    return scaler, train_scaled, test_scaled


#min_max_scaler()
def min_max_scaler(train_data, test_data, feat_range=(0,1)):
    '''
    takes in test data and train data and fits them both
    '''
    scaler = MinMaxScaler(copy=True, feature_range=feat_range
    scaler.fit(train_data)
    test_scaled = pd.DataFrame(scaler.transform(test_data), columns=test_data.columns, index=test_data.index)
    train_scaled = pd.DataFrame(scaler.transform(train_data), columns=train_data.columns, index=train_data.index)
    return scaler, train_scaled, test_scaled


#iqr_robust_scaler()
def iqr_robust_scaler(train_data, test_data):
    '''
    takes in test data and train data and fits them both
    '''
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True)
    scaler.fit(train_data)
    test_scaled = pd.DataFrame(scaler.transform(test_data), columns=test_data.columns, index=test_data.index)
    train_scaled = pd.DataFrame(scaler.transform(train_data), columns=train_data.columns, index=train_data.index)
    return scaler, train_scaled, test_scaled