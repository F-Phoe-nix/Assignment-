import pandas as pd
import numpy as np

df = pd.read_csv('traffic_accidents.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull() .sum())
print(df.duplicated() .sum())