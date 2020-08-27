import preprocessinghandles as app
import preprocessObject
import pandas as pd
from sklearn import preprocessing

#This function receives the raw sales price dataFrame and return it preprocessed (without eventual nans and with dummies)
# This function imports the script preprocessinghandles

def preprocessinghandle(dataframe):
    df = dataframe.copy()
    columns_values = df.columns
    for i in columns_values:
        if df[i].dtype == 'int64' or df[i].dtype == 'float64':
            df[i] = app.varPreprocessing(df[i])
        elif df[i].dtype == 'object':
            df_dummies = app.classPreprocessing(df[i])
            df_dummies = df_dummies.add_prefix(i + '_')
            df = df.drop([i], axis = 1)
            df = pd.concat([df, df_dummies], axis = 1)
    return df

# def preprocessinghandle(dataframe):
#     df = dataframe.copy()
#     columns_values = df.columns
#     for i in columns_values:
#         if df[i].dtype == 'int64' or df[i].dtype == 'float64':
#             df[i] = app.varPreprocessing(df[i])
#         elif df[i].dtype == 'object':
#             df[i] = preprocessObject.preprocessObject(df[i])
#             # df_dummies = app.classPreprocessing(df[i])
#             # df_dummies = df_dummies.add_prefix(i + '_')
#             # df = df.drop([i], axis = 1)
#             # df = pd.concat([df, df_dummies], axis = 1)
#     return df