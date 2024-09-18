import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('FreeCodeCamp DataAnalysis/Page View Time Series Visualizer/fcc-forum-pageviews.csv', parse_dates= ['date'], index_col='date')
#df['date'] = pd.to_datetime(df['date'])
#df = df.set_index(df['date'])
#df = df.drop(['date'], axis=1)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975))&
        (df['value'] >= df['value'].quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 9))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df)


    # Save image and return fig (don't change this part)
    fig.savefig('FreeCodeCamp DataAnalysis/Page View Time Series Visualizer/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    df_bar = df_bar.set_index(['Years'])
    df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Month'], sort='False')['value'].mean().round().astype(int))
    df_bar = df_bar.unstack()
    df_bar = df_bar.rename(columns={'value': 'Average Page Views'})
    #missing_data = {
    #    'Years': [2016, 2016, 2016, 2016],
    #    'Month': ['January', 'February', 'March', 'April'],
    #    'Average Page Views': [0, 0, 0, 0]
    #}
    #df_bar = pd.concat([pd.DataFrame(missing_data), df_bar]).reset_index()
    #df_bar = df_bar.drop(['index'], axis=1)
    #month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     #              'August', 'September', 'October', 'November', 'December']
    #df_bar['Month'] = pd.Categorical(df_bar['Month'], categories=month_order, ordered=True)
    #df_bar = df_bar.sort_values(by=['Years', 'Month'])

    # Draw bar plot
    fig = df_bar.plot.bar(figsize =(16, 9)).get_figure()
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December'])
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    #chart = sns.barplot(data=df_bar, x='Years', y='Average Page Views', hue='Month', palette='tab10')
    #chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')

    # Save image and return fig (don't change this part)
    fig.savefig('FreeCodeCamp DataAnalysis/Page View Time Series Visualizer/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(32, 10))

    #Yearly
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], hue='year', legend=False, palette='tab10')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    #Monthly
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                   'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1], hue='month', legend=False, palette='tab10')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('FreeCodeCamp DataAnalysis/Page View Time Series Visualizer/box_plot.png')
    return fig
