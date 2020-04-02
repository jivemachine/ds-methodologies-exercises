
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport



# plots all of the pairwise relationships along with the regression line for each pair.
def plot_variable_pairs(dataframe):
    sns.pairplot(dataframe, kind="reg", diag_kind="kde", plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.7}})


#Write a function, months_to_years(tenure_months, df) that returns your 
#dataframe with a new feature tenure_years, in complete years as a customer.
def months_to_years(df_months, df):
    df["years"] = (df_months / 12).astype(int)
    return df

#Write a function, plot_categorical_and_continous_vars(categorical_var, 
# continuous_var, df), that outputs 3 different plots 
#for plotting a categorical variable with a continuous variable, 
# e.g. tenure_years with total_charges. For ideas on effective
#  ways to visualize categorical 
#with continuous: https://datavizcatalogue.com/. You can then 
# look into seaborn and matplotlib documentation for ways to create plots.

def plot_categorical_and_continuous_vars(x, y, df):
    plt.figure(figsize=(10,20))
    plt.subplot(4,1,1)
    sns.barplot(x=x, y=y, data=df)
    plt.subplot(4,1,2)
    sns.boxplot(x= x, y= y, data=df)
    plt.subplot(4,1,3)
    sns.swarmplot(x= x, y= y, data=df)
    plt.subplot(4,1,4)
    sns.violinplot(x=x, y=y, data=df)
    plt.show()


#pandas profile

def do_a_pandas_profile(df, name):
    from pandas_profiling import ProfileReport
    profile = ProfileReport(df, title=name, html={'style':{'full_width':True}})
    profile.to_widgets(), profile.to_notebook_iframe()
