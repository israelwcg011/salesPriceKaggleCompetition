def verifyColumns(biggerDataFrame, dataFrame):
    df1Columns = biggerDataFrame.columns.values
    df2Columns = dataFrame.columns.values
    for i in df1Columns:
        if i in df2Columns:
            pass
        else:
            print(i + ' ist nicht in der List.')