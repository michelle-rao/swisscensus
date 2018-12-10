#This file checks for the files generated, and merges them together
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import glob
#add checks for the files for a combined file

datatype = ["_population", "_language_civilstatus", "_employment"]
year = ["1980"]
path ="C:/Users/Michelle/Desktop/Project/swisscensus/swisscensus/" # use your path

#Creating three separate files of datatype, "final_population", "final_language_civilstatus",
#and "final_employment"
frame = pd.DataFrame()
list = []

for type in datatype:
    allFiles = glob.glob(path + type + "/*.csv" )
        # for cant in canton:
    for file in allFiles:
        df = pd.read_csv(file,index_col=None, header=0)
        list.append(df)
    frame = pd.concat(list,sort = False)
    frame.to_csv(type + "_final.csv", index=False)
    list = []
    frame = []

#Would add checks here
dflist = []

#Cleaning datafiles
for type in datatype:
    df = pd.read_csv(type + "_final.csv")
    df.rename({"Unnamed: 0":"a"}, axis = "columns", inplace = True)
    df.drop(["a"],axis=1, inplace = True)
    df.drop(['1','2','3','4','5','6','7','8','9','10','11','12'],axis=1, inplace=True)
    df.set_index('mun_name', inplace = True)
    dflist.append(df)

left =dflist[0]
middle = dflist[1]
right = dflist[2]

result1 = pd.merge(left, middle, on= 'mun_name', how="outer")
result2 = pd.merge(result1, right, on= 'mun_name', how="outer")
result2.drop(['13_x', '13_y'], axis=1, inplace=True)

print(result2.head())
result2.to_csv("_allvar_final.csv", index = True)
