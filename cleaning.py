import pandas as pd
file_name = 'data/researchers.csv'
df = pd.read_csv(file_name)
print(df.columns)
# print(df.shape)
# print(df.head())
# print(df.dtypes)
# print(df.isnull().sum())
# print("###########33 duplica
# ted###########")
# print(df.duplicated().sum())
#print(df[(df['is_active']==True) & (df['h_index']>15)].sort_values(by='joined_year', ascending=True))
filter_df =df[(df['is_active']==True) & (df['h_index']>15)].sort_values(by='joined_year', ascending=True)
cp1 = filter_df['last_name'].str[0].str.cat(sep='')
print(cp1)

####################
df_json = pd.read_json('data/publications.json')
print(df_json)
print(df_json.shape)
print(df_json.head())
print(df_json.dtypes)
print(df_json.isnull().sum())
print(df_json.duplicated().sum())
print(df_json.columns)
df_json['citations'] = pd.to_numeric(df_json['citations'])
cp2 = df_json.loc[df_json['citations'].idxmax(), 'researcher_id']
#################
print(cp2)
