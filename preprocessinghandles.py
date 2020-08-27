import pandas as pd
from sklearn import preprocessing

# This script contains all the functions needed to preprocess the house prices data

# preprocessing dtypes
## var
## This function gets a dataFrame as input and return a dataFrame as output (without the eventual nans)
def varPreprocessing(df):
    array = []
    dfMean = df.mean()
    
    for i in df:
        if pd.isna(i):
            i = dfMean
            array.append(i)
        else:
            array.append(i)
    
    arrayScaled = preprocessing.scale(array)
    dfArray = pd.DataFrame(array)

    return dfArray

## class
## This function gets a dataFrame as input and return the dummies dataFrame as output (without the possible nans)
## I'm not using the elif section on the actual code

# def classPreprocessing(df):
#     if df.dtype == 'object':
#         array = []
#         mostFrequentValue = df.mode()[0]

#         for i in df:
#             if pd.isna(i):
#                 i = mostFrequentValue
#                 array.append(i)
#             else:
#                 array.append(i)
#         dfArray = pd.DataFrame(array)
#         dfArrayDummies = pd.get_dummies(dfArray, drop_first = True)
#         return dfArrayDummies

#     elif df.dtype == 'int64':
#         array = []
#         mostFrequentValue = df.mode()[0]

#         for i in df:
#             if pd.isna(i):
#                 i = mostFrequentValue
#                 array.append(i)
#             else:
#                 array.append(i)
#         #arrayScaled = preprocessing.scale(array)
#         dfArray = pd.DataFrame(array)
#         return dfArray


def classPreprocessing(df):
    array = []
    mostFrequentValue = df.mode()[0]
    for i in df:
        if pd.isna(i):
            i = mostFrequentValue
            array.append(i)
        else:
            array.append(i)
    dfArray = pd.DataFrame(array)
    dfArrayDummies = pd.get_dummies(dfArray, drop_first = True)
    return dfArrayDummies