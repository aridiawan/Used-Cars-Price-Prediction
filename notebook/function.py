def checkOutlier(data, col):
    q1, q3 = data[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lowBound = q1-1.5*iqr
    upBound =  q3+1.5*iqr

    nLow = len(data[data[col] < lowBound])
    nUp = len(data[data[col] > upBound])

    nTot = nLow + nUp

    lowOut = nLow/data.shape[0]*100
    upOut = nUp/data.shape[0]*100

    totOut = lowOut + upOut

    return nTot, totOut