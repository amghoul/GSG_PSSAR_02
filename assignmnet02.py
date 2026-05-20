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
##################################
df_reserchers= load_file(file_csv)
get_file_stats(df_reserchers)

df_publications = load_file(file_json)
get_file_stats(df_publications)

df_funding = load_file(file_excel)
get_file_stats(df_funding)
################################