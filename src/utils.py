import pandas as pd
from IPython.display import display
from .plots import boxplot_temperature_analysis

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

    return df_copy[df_copy["z-score"].apply(lambda x : abs(x)>3)]

def detect_iqr_outliers(df, name_month):

    df_copy = df.copy()

    Q1= df["AvgTemperature"].quantile(0.25)
    Q3= df["AvgTemperature"].quantile(0.75)

    IQR=  Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    print("-" *100)
    print(name_month)
    print(f"the first quartile is: {Q1.round(2)}")
    print(f"the third quartile is: {Q3.round(2)}")
    print(f"the IQR is: {IQR.round(2)}")
    print(f"the lower limit is: {lower_limit.round(2)}")
    print(f"the upper limit is: {upper_limit.round(2)}")
    

    outliers = df_copy[(df_copy["AvgTemperature"] < lower_limit) | (df_copy["AvgTemperature"]> upper_limit)]

    display(outliers)

    return outliers

def outlire_detection (df):

    monthly_outliers={}

    df_copy =df.copy()

    for i in range(1,13):
        df_month=df_copy[df_copy["Date"].dt.month == i]
        name_month= df_month["Date"].dt.month_name().iloc[0]
        month = detect_iqr_outliers(df_month, name_month)
        boxplot_temperature_analysis(df_month, name_month)

        monthly_outliers[name_month]= month

    return monthly_outliers





