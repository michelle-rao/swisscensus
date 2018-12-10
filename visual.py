import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = '_example.csv'
df= pd.read_csv(filename)

#Reshaping data
print(df.head())
idx = ['can_name', 'mun_name', 'year']
multi_indexed_df = df.set_index(idx)
print(multi_indexed_df.head(20))

stacked_df = multi_indexed_df.stack(dropna = True)
print(stacked_df.head(25))

#Creating a smaller dataframe with variables of interest
df1= df[['mun_name', 'can_name', 'year','fem_pop','mun_pop','fem_employed']].copy()

#Converting data into relevant data types
print(df1.dtypes)
df1['fem_pop']=df1.fem_pop.astype(float)
df1['fem_employed']=df1.fem_employed.astype(float)
print(df1.dtypes)

#Creating variable - female labour force participation
df1['FLFP'] = df1['fem_pop']/ df1['mun_pop']
print(df1.head())

by_canton = df1.groupby('can_name')
print(by_canton.mean())
sns.set()

xvar = "can_name"
yvar = "FLFP"

#barplot
sns.catplot(x=xvar, y=yvar,  palette = 'coolwarm', data=df1,kind='bar')
plt.xticks(rotation=50, fontsize=6)
plt.title('Female Labour Force Participation by Canton')
plt.ylabel('Female Labour Force Participation (%)', fontsize=10)
plt.xlabel('Canton Name', fontsize=10)
plt.show()

#heatmap - can add columns='year', once data is available
flfp_cant= df1.pivot_table(values='FLFP', index='can_name', columns='year')
sns.heatmap(flfp_cant, cmap='magma', linecolor='white', linewidths=1)
plt.title('Female Labour Force Participation by Canton')
plt.ylabel('Female Labour Force Participation (%)', fontsize=10)
plt.xlabel('Canton Name', fontsize=10)
plt.yticks(fontsize=6)
plt.show()
#
# #regplot
# sns.catplot(x="can_name", y=yvar, data=df1, col="year", palette = "coolwarm")
# plt.show()

# #line graph
# sns.relplot(x= xvar, y= yvar, data= df1)
# plt.show()
#
# #scatter plot
# df1.plot.scatter(x=xvar,y=yvar,c= cvar ,cmap='coolwarm')
# plt.show()
# #y= data['married']/data['total_pop']
#
# #scatter plot with fitted line
# sns.lmplot(x=xvar, y=yvar, data=df1)
# plt.show()
#
# #violinplot
# #sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
# #plt.show()
#
