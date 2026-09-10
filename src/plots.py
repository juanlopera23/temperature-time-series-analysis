import matplotlib.pyplot as plt
import pandas as pd


def temperature_comparison_with_Rolling_7 (df):
    
    plt.figure (figsize=(12, 6))
    plt.plot(
        df["Date"],
        df["AvgTemperature"],
        label="Daily TEmperature",
        marker="."
    )
    plt.plot(
        df["Date"],
        df["Rolling_7"],
        label="7-Day moving average",
    
    )
    plt.xlabel("Date")
    plt.ylabel("Temperature (°F)")
    plt.legend()
    plt.show()

def boxplot_temperature_analysis (df, month):

    ax= df.boxplot(column="AvgTemperature")

    ax.set_title (f"Temperature analysis {month}")
    ax.set_ylabel("Temperature")
    plt.suptitle("")

    plt.show()
