import pandas as pd

def get_data():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
                          header=None, sep='\s+')
    df.columns = ['CRIM',
                  'ZN',
                  'INDUS',
                  'CHAS',
                  'NOX',
                  'RM',
                  'AGE',
                  'DIS',
                  'RAD',
                  'TAX',
                  'PTRATIO',
                  'B',
                  'LSTAT',
                  'MEDV']
    return df