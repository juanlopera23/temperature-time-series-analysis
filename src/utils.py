import pandas as pd

def age_calculator(years, df : pd.DataFrame):
    for year in years:
        df_copy=df[df["Year"] == year]
        print(df_copy.groupby("Year")["City"].value_counts())

def cities_comprobation(cities: list,df: pd.DataFrame):
    for city in cities:
        df_copy=df[df["City"]== city]
        print(f"NAME : {city}")
        print(df_copy["State"].value_counts())
        print("-"*40)


def z_score(df):

    df_copy= df.copy()

    mean_df = df_copy["AvgTemperature"].mean()
    std_df= df_copy["AvgTemperature"].std()

    df_copy["z-score"]=df_copy["AvgTemperature"].apply(lambda x: (x - mean_df)/std_df)

    return df_copy[df["z-score"].apply(lambda x : abs(x)>3)]