import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('FreeCodeCamp DataAnalysis/Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    fig = df.plot.scatter(x= 'Year', y= 'CSIRO Adjusted Sea Level', figsize =(16, 9)).get_figure()

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df_2050 = df['Year'].copy()
    missing_data = pd.DataFrame({'Year': np.arange(2014, 2051)})
    df_2050 = pd.concat([pd.DataFrame(missing_data), df_2050]).sort_values(by='Year')
    y_fit = slope * df_2050 + intercept
    plt.plot(df_2050, y_fit, color='red')
             
    # Create second line of best fit
    df_00_13 = df[df['Year'] >= 2000].copy()
    slope2, intercept2, r_value, p_value, std_err = linregress(df_00_13['Year'], df_00_13['CSIRO Adjusted Sea Level'])
    df_00_50 = df_00_13['Year'].copy()
    missing_data = pd.DataFrame({'Year': np.arange(2014, 2051)})
    df_00_50 = pd.concat([pd.DataFrame(missing_data), df_00_50]).sort_values(by='Year')
    y_fit2 = slope2 * df_00_50 + intercept2
    plt.plot(df_00_50, y_fit2, color='blue')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('FreeCodeCamp DataAnalysis/Sea Level Predictor/sea_level_plot.png')
    return plt.gca()

