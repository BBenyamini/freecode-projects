import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["BMI"]=df.weight/(df.height/100)**2

def calculate_overwight(bmi):
    if bmi<25:
        return 0
    else:
        return 1

df['overweight'] = df["BMI"].apply(calculate_overwight)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

def normalize_col(column):
    if column==1:
        return 0
    else:
        return 1
    
df["cholesterol"]=df["cholesterol"].apply(normalize_col)
df["gluc"]=df["gluc"].apply(normalize_col)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio",value_vars=['active','alco','cholesterol', 'overweight','gluc','smoke'], value_name="value")


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = plt.figure(figsize=[10,6])
    sns.catplot(df_cat, x="variable",col="cardio",hue="value", kind="count")
    plt.ylabel("Total")
    plt.xlabel("Variable")
    plt.show();

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
