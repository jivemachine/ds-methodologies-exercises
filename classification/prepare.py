import pandas as pd
import numpy as np

import sklearn.model_selection
import sklearn.preprocessing


# code for prepping iris dataset

def drop_columns(df):
    df = df.drop(columns=(['species_id', 'measurement_id']))
    df.rename(columns={'species_name': "species"}, inplace=True)
    return df


def encode_species(train, test):
    encoder = sklearn.preprocessing.OneHotEncoder(sparse=False)
    encoder.fit(train[['species']])
    # nice columns for display
    cols = ['species ' + c for c in encoder.categories_[0]]
    m = encoder.transform(train[['species']])
    train = pd.concat([
    train,
    pd.DataFrame(m, columns=cols, index=train.index)
    ], axis=1).drop(columns='species')
    
    m = encoder.transform(test[['species']])
    test = pd.concat([
        test,
        pd.DataFrame(m, columns=cols, index=test.index)
    ], axis=1).drop(columns='species')
    return train, test





def prep_iris(df):
    df = drop_columns(df)
    train, test = sklearn.model_selection.train_test_split(
        df, random_state=830, train_size=.8
    )
    train, test = encode_species(train, test)
    
    return train, test




# all of the code for prepping the titanic dataset   
    
def embark_titanic(df):
    df.embark_town = df.embark_town.fillna("Southampton")
    df.embarked = df.embarked.fillna("S")
    df = df.drop(columns=('deck'))
    return df
    
def impute_titanic(df):
    train, test = sklearn.model_selection.train_test_split(
        df, random_state=123, train_size=.8)
    
    imputer = sklearn.impute.SimpleImputer(strategy='mean')
    imputer.fit(train[['age']])
    train.age = imputer.transform(train[['age']])
    test.age = imputer.transform(test[['age']])
    return train, test

def encode_titanic(train, test):
    encoder = sklearn.preprocessing.OneHotEncoder(sparse=False)
    encoder.fit(train[['embarked']])
    #getting those nice columns
    cols = ['embarked ' + c for c in encoder.categories_[0]]
    m = encoder.transform(train[['embarked']])
    train = pd.concat([
        train,
        pd.DataFrame(m, columns=cols, index=train.index)
    ], axis=1).drop(columns='embarked')
    
    m = encoder.transform(test[['embarked']])
    test = pd.concat([
        test,
        pd.DataFrame(m, columns=cols, index=test.index)
    ], axis=1).drop(columns='embarked')
    return train, test
    
def scale_minmax(train, test, column_list):
    scaler = sklearn.preprocessing.MinMaxScaler()
    column_list_scaled = [col + '_scaled' for col in column_list]
    train_scaled = pd.DataFrame(scaler.fit_transform(train[column_list]), 
                                columns = column_list_scaled, 
                                index = train.index)
    train = train.join(train_scaled)

    test_scaled = pd.DataFrame(scaler.transform(test[column_list]), 
                                columns = column_list_scaled, 
                                index = test.index)
    test = test.join(test_scaled)

    return train, test
    

def prep_titanic(df):
    df = embark_titanic(df)
    train, test = impute_titanic(df)
    train, test = encode_titanic(train, test)
    train, test = scale_minmax(train, test, column_list = ['age', 'fare'])
    return train, test
    