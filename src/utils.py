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
