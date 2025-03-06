import pandas as pd

df = pd.read_csv('traffic_accidents.csv')

print(df.head())

df.replace('UNKNOWN', pd.NA, inplace = True) #UNKOWN = NaN

df.dropna(inplace = True) #drop NaN values

df['crash_date'] = pd.to_datetime(df['crash_date'])
df['crash_hour'] = df['crash_hour'].astype(int)
df['crash_day_of_week'] = df['crash_day_of_week'].astype(int)
df['crash_month'] = df['crash_month'].astype(int)
df['injuries_total'] = df['injuries_total'].astype(float)
df['injuries_fatal'] = df['injuries_fatal'].astype(float)
df['injuries_incapacitating'] = df['injuries_incapacitating'].astype(float)
df['injuries_non_incapacitating'] = df['injuries_non_incapacitating'].astype(float)
df['injuries_reported_not_evident'] = df['injuries_reported_not_evident'].astype(float)
df['injuries_no_indication'] = df['injuries_no_indication'].astype(float)

df.drop_duplicates(inplace = True)

#save
cleaned = 'cleaned_accidents.csv'
df.to_csv(cleaned, index = False)

print("Dataset cleaned and saved to", cleaned)