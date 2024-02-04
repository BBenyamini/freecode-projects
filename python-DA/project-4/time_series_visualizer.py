import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

# Clean data
df =df[(df.value>=df.value.quantile(0.025)&(df.value<=df.value.quantile(0.975)))]
df.index=pd.to_datetime(df.index)


def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=[15,7])
    sns.lineplot(data=df,x=df.index, y="value", color="brown" )
    plt.title("Daily freeCodeCamp Forum Page Views", size=20)
    plt.xlabel("Date")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot


    df["Month"],df["Year"]=df.index.month,df.index.year
    df["Month"]=df["Month"].replace({1:"January", 2:"February",3:"March", 4:"April", 5:"May", 6:"June",7:"July",8:"August",9:"September",
                    10:"October",11:"November",12:"December"})
    df_bar=df.groupby(by=["Year","Month"])["value"].mean().reset_index()

    # Draw bar plot

    fig=plt.figure(figsize=[10,8])
    sns.barplot(data=df, x="Year",y="value", hue="Month",palette="Set1" )
    plt.ylabel("Average Page Views")
    plt.xlabel("Year")
    plt.legend(loc="upper left")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig=plt.figure(figsize=(18,7))

    plt.subplot(1,2,1)
    sns.boxplot(data=df_box,x="year", y="value", palette="Set1")
    plt.title("Year-wise Box Plot (Trend)")

    plt.subplot(1,2,2)
    sns.boxplot(data=df_box,x="month", y="value", palette="Set1")
    plt.title("Month-wise Box Plot (Trend)")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
