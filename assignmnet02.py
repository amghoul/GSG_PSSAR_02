import pandas as pd
file_csv = 'data/researchers.csv'
file_json = 'data/publications.json'
file_excel = 'data/funding.xlsx'

# loading a file into datframe
def load_file(file_name):
    name=file_name.split("/")[1]
    ext = file_name.split(".")[1]
    if ext == "json":
        df = pd.read_json(file_json)
    elif ext == "xlsx":
        df = pd.read_excel(file_excel)
    else: #ext == "csv":
        df= pd.read_csv(file_csv)
    print(f"\n####### {name} ws loaded ####### \n")
    print(df.head())
    return df

# Get statistics about a dataframe
def get_file_stats(df):
    stats_list = ["dtypes", "describe", "isnull", "duplicated", "columns","shape"]
    for item in stats_list:
        print(f"\n############ df.{item} ############")
        attr = getattr(df, item)
        if item in ["describe"]:
            print(attr())
        elif item == "isnull":
            print(attr().sum())
        elif item == "duplicated":
            print(attr().sum())
        else:
            print(attr)

# Clean funding file
def clean_funding(df):
    df_clean = df.dropna(subset=['amount_cad', 'status']).copy()
    df_clean['amount_cad'] = pd.to_numeric(df_clean['amount_cad'], errors='coerce')
    df_clean = df_clean[df_clean['amount_cad'] > 0]
    return df_clean

# merge three dataframes according to the type value
def merge_func(df1, df2, df3, type):
    merged_df1_df2= pd.merge(df1, df2, on='researcher_id', how=type )
    merged_all = pd.merge(merged_df1_df2, df3, on='researcher_id', how=type )
    print(f"######## The merged three files using {type} join ######### \n")
    print(merged_all.head())
    get_file_stats(merged_all)
    return merged_all

############### Loading files and get stats about each one#############
df_reserchers= load_file(file_csv)
get_file_stats(df_reserchers)

df_publications = load_file(file_json)
get_file_stats(df_publications)

df_funding = load_file(file_excel)
get_file_stats(df_funding)
################# Clean funding file ##########
df_funding_cleaned = clean_funding(df_funding)
print(get_file_stats(df_funding_cleaned))

########## Merging the three dataframes using inner merge
merge_inner = merge_func(df_publications, df_funding_cleaned, df_reserchers, "inner")
""" In the inner join we got 47 rows and 23 columns. 
The inner join keeps all rows that matches "researcher_id" in the three dataframes 
Here, we have no missed values
"""
merge_left = merge_func(df_publications, df_funding_cleaned, df_reserchers, "left")
"""In the left join we get 77 rows and 23 columns, 
we keep all rows in the publications dataframe in addition to the matached rows 
in other two datafremes where "research_id" matched
In this join we have many null values becasue there are some research_id not exist in other dataframes.
"""




