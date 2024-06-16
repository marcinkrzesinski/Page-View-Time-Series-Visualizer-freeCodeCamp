import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=['date'], parse_dates=True)


# Clean data
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)

df = df[ (df['value']>=lower_quantile) & (df['value']<=upper_quantile)  ]


# ---------------------------------------------------------------
# LINE PLOT
def draw_line_plot():
    # Draw line plot
    # fig, ax = plt.subplots( figsize=(10,5) )
    fig = plt.figure( figsize=(12,6) )

    plt.plot(df.index, df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig







# ---------------------------------------------------------------
# BAR PLOT 
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby( ['year', 'month'] )['value'].mean() 
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, ylabel='Average Page Views', xlabel='Years', figsize=(12,6)).figure
    plt.legend( ['January','February','March','April','May','June','July','August','September','October','November', 'December'] )

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png') 
    return fig




# ---------------------------------------------------------------  
# BOX PLOT
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots( nrows=1, ncols=2, figsize=(12,6) )
    axes[0] = sns.boxplot( x=df_box['year'], y=df_box['value'], ax=axes[0] )
    axes[1] = sns.boxplot( x=df_box['month'], y=df_box['value'], ax=axes[1], order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov', 'Dec'] )

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
