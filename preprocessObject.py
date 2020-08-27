import pandas as pd
import numpy as np
from sklearn import preprocessing
from scipy.stats import mode

def preprocessObject(dataFrame):
    df = dataFrame.copy()
    mostFrequenteValue = df.mode()[0]
    for item in df:
        if pd.isna(item):
            item = mostFrequenteValue
        else:
            item = item
    uniqueValues = df.unique()
    for i in range(len(uniqueValues)):
        df = np.where(df == uniqueValues[i], i, df)
        #df = df.map({ "'" + uniqueValues[i] + "'": i })
    return df
