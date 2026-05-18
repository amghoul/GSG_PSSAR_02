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
###############
df_excel = pd.read_excel('data/funding.xlsx')
print(df_excel.head())
print(df_excel)
print(df_excel.shape)
print(df_excel.head())
print(df_excel.dtypes)
print(df_excel.isnull().sum())
print(df_excel.duplicated().sum())
print(df_excel['amount_cad'].describe())
print(df_excel.columns)

df_clean = df_excel.dropna(subset=['amount_cad'])
#df_clean =df_clean[df_clean['amount_cad']>0] 
df_clean = pd.to_numeric(df_clean['amount_cad'], errors='coerce')
df_clean = df_excel[df_excel['amount_cad'] > 0]

# 3. Calculate the sum of the positive numbers
positive_sum = df_clean['amount_cad'].sum()
cp3 = positive_sum
print(f"The sum of positive numbers is: {cp3}")
###
hid_message = "cp1: "+ str(cp1) + " cp2: " + str(cp2) + " cp3: " + str(cp3)[0:4]
print(hid_message)