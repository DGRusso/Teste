import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('FreeCodeCamp DataAnalysis/Medical Data Visualizer/medical_examination.csv')


# 2
df['overweight'] = df['weight']/(df['height']/100)**2
df['overweight'] = (df['overweight'] > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars=['cardio'])
    print(df)
    print(df_cat)

    # 6
    df_cat = pd.DataFrame(df_cat.value_counts())
    print(df_cat)
    #df_cat = pd.melt(df_cat)
    #print(df_cat)
    

    # 7
    


    # 8
    fig = sns.catplot(df_cat, kind='bar')


    # 9
    fig.savefig('FreeCodeCamp DataAnalysis/Medical Data Visualizer/catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = pd.DataFrame(df)
    print(df_heat)
    drop1 = df_heat.loc[(df['height'] <= df['height'].quantile(0.025))]
    drop2 = df_heat.loc[(df['height'] >= df['height'].quantile(0.975))]
    drop3 = df_heat.loc[(df['weight'] <= df['weight'].quantile(0.025))]
    drop4 = df_heat.loc[(df['weight'] >= df['weight'].quantile(0.975))]
    df_heat = df_heat.drop(drop1)
    df_heat = df_heat.drop(drop2)
    df_heat = df_heat.drop(drop3)
    df_heat = df_heat.drop(drop4)
    print(df_heat)

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('FreeCodeCamp DataAnalysis/Medical Data Visualizer/heatmap.png')
    return fig

draw_cat_plot()
#draw_heat_map()