import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df=pd.read_csv('medical_examination.csv')


# Add 'overweight' column
df['overweight']=df['weight']/((df['height']/100)**2)
df.loc[df['overweight']>25,'overweight']=1
df.loc[df ['overweight']!=1,'overweight']=0


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']!=0,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']!=0,'gluc']=1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cats=pd.melt(df,id_vars='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    group=df_cats.groupby(['cardio'])
    v=group.value_counts()
    j=v.to_frame()
    check=j.reset_index()
    check.rename(columns={0:'total'},inplace=True)    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=check,x='variable',y='total',kind='bar',col='cardio',hue='value',order=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Get the figure for the output
    fig = plt.gcf()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[df['ap_lo']<=df['ap_hi']]
    c1=df['height'].quantile(0.025)
    c2=df['height'].quantile(0.975)
    c3=df['weight'].quantile(0.025)
    c4=df['weight'].quantile(0.975)
    df_heat=df_heat[df_heat['height']>=c1]
    df_heat=df_heat[df_heat['height']<=c2]
    df_heat=df_heat[df_heat['weight']>=c3]
    df_heat=df_heat[df_heat['weight']<=c4]
    # Calculate the correlation matrix
    corr=df_heat.corr()

    # Generate a mask for the upper triangle
    mask=np.triu(np.ones(corr.shape)).astype(bool)



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask,ax=ax,annot=True,fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
