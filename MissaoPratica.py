import pandas as pd

csv_file = 'dados.csv'
df = pd.read_csv(csv_file, sep=';')

print(df.head())
print(df.tail())

backup_df = df

backup_df['Calories'] = 0

print('\n', backup_df.head())

#backup_df['Date'] = backup_df['Date'].fillna('1900-01-01')

print('\n', backup_df)

backup_df['Date'] = backup_df['Date'].replace('20201223', pd.to_datetime('20201223'))
backup_df['Date'] = pd.to_datetime(backup_df['Date'], format='%Y-%m-%d')

print('\n', backup_df.head())

backup_df.dropna(subset='Date', inplace=True)

print('\n', backup_df)