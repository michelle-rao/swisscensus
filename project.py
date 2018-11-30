filename = "data.pdf"
pagerange = "all"
from tabula import read_pdf
from tabula import convert_into

df = read_pdf(filename, page = pagerange)
print(df)
#df = read_pdf(filename, output_format='dataframe', encoding ='Ansi',java_options = None, pandas_options = None, multiple_tables = False)
#df.to_csv('df_output.csv', encoding ='utf-8')

convert_into(filename, "output.csv", output_format = "csv")

#!cat test.csv


#import tabula
#import os
#import pandas as pd

#folder = 'data/pdf/'
#paths = [folder + fn for fn in os.listdir(folder) if fn.endswith('.pdf')]
#for path in paths:
    #df = tabula.read_pdf(path, encoding = 'latin1', pages = 'all', area = [29.75,43.509,819.613,464.472], nospreadsheet = True)
    #path = path.replace('pdf', 'csv')
    #df.to_csv(path, index = False)
