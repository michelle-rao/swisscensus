import urllib.request, urllib.parse, urllib.error
import tabula
from tabula import read_pdf
import glob, os
import pandas as pd

links = [
#1980:
#BL:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345650/master",
#BS:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345652/master",
#GL:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/350643/master",
#LU:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345662/master",
#NW:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345666/master",
#OW:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345668/master",
#SG:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345670/master",
#SH:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345672/master",
#SZ:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345674/master",
#SO:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345676/master",
#TG:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345678/master",
#UR:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345682/master",
#ZG:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345688/master",
#ZH:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345690/master",
#AG:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345644/master",
#AR:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345646/master",
#AI:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345648/master",
#FR:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345656/master",
#BE:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345654/master",
#VS:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345684/master",
#GR:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345658/master"]

numbers = []
for i in links:
    vector = i.split('/')
    numbers.append(vector[6])

varnames = pd.read_csv('variable_list_census1980.csv',
    header=1)
varnames = varnames[varnames.columns[0]]
varnames = list(varnames)

for i in numbers:
    try:
        url = ('https://www.bfs.admin.ch/bfsstatic/dam/assets/' + str(i) + '/master')
        name = (str(i) + '_1980.pdf')
        print(name)
        urllib.request.urlretrieve(url, name)
        # First dataframe (Swiss and foreign population):
        # For Fribourg (FR), Bern (BE), Valais (VS) and Graubünden (GR):
        if i == '345656' or i == '345654' or i == '345684' or i == '345658':
            df = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
        # For all others:
        else:
            df = read_pdf(name, pages="19",area=(118.64,55.25,718.41,505.21))
        new = df.columns.values[0]
        new = new.split()
        # For Fribourg (FR) and Valais (VS):
        if i == '345656' or i == '345684':
            new = new[2]
        # For all others:
        else:
            new = new[1]
        print(new)
        for name in glob.iglob(name):
            os.rename(name, (new + '_1980.pdf'))
        canton = list(df.columns.values)
        # For Uri (UR) and St. Gallen (SG):
        if i == '345682' or i == '345670':
            df = df.drop('Unnamed: 1', axis=1)
            df.columns = varnames[0:12]
        # For all others:
        else:
            df.columns = varnames[0:12]
        # Assign canton-level variables:
        df = df.assign(can_name = new)
        for j in range(1,len(canton)):
            df = df.assign(varname = canton[j])
            varnew = j
            df.rename(columns={"varname": varnew}, inplace=True)
        newname = (new + '_population_1980.csv')
        df.to_csv('./_population/' + newname)
    except:
        print('Warning!')
        break
