import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Loading the data
df = pd.read_csv('./medical_examination.csv')

# Adding a column to the data named "overweight", determining if a person is overweight in an binary order
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# Normalizing the data, if the value of `gluc` or `cholesterol` is 1, setting the value 1, and if more that 1 setting the value to 0
df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

# Drawing a categorical plot
def draw_cat_plot():
    # Creating a long formate data fram from some of the columns for the categorical plotting
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     var_name='variable', value_name='value') 


    # Grouping the data in `df_cat` and splitting it by `cardio`
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # Converting this data into long format, creating a chart using seaborn `sns.catplot()` method
    # df_long = pd.melt(df_cat, var_name='feature', value_name='value')
    grid = sns.catplot(x='variable', hue='value', y='total', col='cardio', data=df_cat, kind='bar', height=5, aspect=1.5)

    # Store the figure
    fig = grid.fig

    fig.savefig('catplot.png')
    return fig


# Drawing the heatmap
def draw_heat_map():
    # filtering some paitent segments with incorrect info
    df_heat = df[(
            (df['ap_lo'] <= df['ap_hi']) &
            (df['height'] <= df['height'].quantile(0.975)) & (df['height'] >= df['height'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))
        )
    ]


    # calculating the corrolation matrix
    corr = df_heat.corr()

    # Generating a mask for upper triangle of the corrolation matrix
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # Matplot lib figure
    fig, ax = plt.subplots(figsize=(8, 8))


    # Plotting heatmap using seaborn
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax, cbar_kws={"shrink": 0.5})

    fig.savefig('heatmap.png')
    return fig