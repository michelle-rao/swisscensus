import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = '_allvar_final.csv'
df= pd.read_csv(filename)
sns.set()

print(df.head())
#See if we can add these as questions in the command line

df1= df[['mun_name', 'can_name','fem_pop','mun_pop','fem_employed']].copy()
df1.dropna()
print(df1.dtypes)

df['fem_pop'] = df['fem_pop'].convert_objects(convert_numeric=True)
df1['fem_pop']=df1.fem_pop.astype(float)
# df1['fem_employed']=df1.fem_employed.astype(float)

print(df1.dtypes)

#df1['FLFP'] = df1['fem_pop']/ df1['mun_pop']


xvar = "mun_name"
yvar = "fem_employed"

#page 26,27 (female labour force participation)
#graphty= ['line', 'scatter', 'scatterfit', 'bar']
#Add option for choosing which version you want
#Checking the main variables in the plot

#Heatmap with 10 cantons; and two years with female labour force participation
#Heatmap with cantons & percentage foreign population
#Regression line graph with years and FLP
#
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
# #barplot
# sns.barplot(x=xvar, y=yvar, data=df1)
# plt.show()
#
# #violinplot
# #sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
# #plt.show()
#
# #matrixplots
# #flights.pivot_table(values='passengers',index='month',columns='year')
# #plt.show()
