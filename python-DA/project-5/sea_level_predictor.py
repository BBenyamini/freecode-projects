import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(x="Year",y="CSIRO Adjusted Sea Level", data=df)


    # Create first line of best fit
    slope, intercept, r, p, se=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    time=np.arange(1880, 2051,1)
    plt.scatter(x="Year",y="CSIRO Adjusted Sea Level", data=df, label="original data")
    plt.plot(time, intercept+ slope*time, label="Fitted data", color="red")


    # Create second line of best fit
    fig=plt.figure(figsize=[6,6])
    df_2000=df[df["Year"]>=2000]
    res=linregress(df_2000["Year"],df_2000["CSIRO Adjusted Sea Level"])
    plt.scatter(df_2000["Year"],df_2000["CSIRO Adjusted Sea Level"])
    plt.scatter(x="Year",y="CSIRO Adjusted Sea Level", data=df, label="original data", color="blue")
    plt.plot(time, intercept+ slope*time, label="Fitted data-1880-2050", color="green")
    plt.plot(time[time>=2000], res.intercept+ res.slope*time[time>=2000], label="Fitted data-2000-2050", color="red")


    # Add labels and title

    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()