import tabula
from tabula import read_pdf

# Read pdf into DataFrame
df = read_pdf("hs-d-00.01-vz-1980-23.pdf", pages="19")
print(type(df))
df.columns = ["Gemeinde","total_pop","m_pop","w_pop","tot_swiss","m_swiss","w_swiss","total_foreign","m_foreign","w_foreign","percent_swiss","percent_foreign"]
print(df)

df2 = read_pdf("hs-d-00.01-vz-1980-23.pdf", pages="20")
df2.columns = ["total_pop","m_pop","w_pop","tot_swiss","m_swiss","w_swiss","total_foreign","m_foreign","w_foreign","percent_swiss","percent_foreign"]
print(len(df.columns))
print(len(df2.columns))
print(df["Gemeinde"])

import pandas as pd
df = pd.concat([df,df2],axis=1)
print(df)
df.to_csv("GL_1980.csv")

import urllib2

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
webContent = response.read()

print(webContent[0:300])
