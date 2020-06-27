import pandas as pd
from sklearn import preprocessing


def preProcessData(DataFrame):
    scaler = preprocessing.StandardScaler()
    numericType = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    cols = DataFrame.select_dtypes(include=numericType).columns.tolist()
    for col in cols:
        # fill null cells with avrage value of the col
        DataFrame[col].fillna(DataFrame[col].mean(), inplace=True)
        # standardization
        DataFrame[cols] = scaler.fit_transform(DataFrame[cols])

    countries = DataFrame['country']
    countries = list(dict.fromkeys(countries))
    procData = pd.DataFrame(index=countries, columns=cols)
    procData.drop(['year'], 1, inplace=True)

    for Country in countries:
        dataOfCountry = DataFrame.loc[DataFrame['country'] == Country]
        dataOfCountry.drop(['country'], 1, inplace=True)
        dataOfCountry.drop(['year'], 1, inplace=True)
        rows = []
        for col in dataOfCountry:
            rows.append(dataOfCountry[col].mean())
        procData.loc[Country] = rows
        procData.index.name='country'
    return procData
