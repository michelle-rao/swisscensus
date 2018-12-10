import urllib.request, urllib.parse, urllib.error
import tabula
from tabula import read_pdf
import glob, os
import pandas as pd
import re

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
        # Second dataframe (Language and civil status):
        # For Fribourg (FR), Bern (BE), Valais (VS) and Graubünden (GR):
        if i == '345656' or i == '345654' or i == '345684' or i == '345658':
            df1 = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="27", area=(118.64,55.25,718.41,505.21))
        # For all others:
        else:
            df1 = read_pdf(name, pages="19", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="20",area=(118.64,55.25,718.41,505.21))
        # For Zug (ZG):
        if i == '345688':
            new = 'ZUG'
        # For all others:
        else:
            new = df1.columns.values[0]
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
        # For Luzern (LU):
        if i == '345662':
            df = df.drop('Unnamed: 7', axis=1)
            df.columns = varnames[13:27]
        # For all others:
        else:
            df.columns = varnames[13:27]
        # Assign canton-level variables:
        for j in range(0,len(canton)):
            df = df.assign(varname = canton[j])
            varnew = ('can_' + varnames[(j+13)])
            df.rename(columns={"varname": varnew}, inplace=True)
        print(df.columns)
        munname = df1[df1.columns.values[0]]
        df = df.assign(mun_name = munname, can_name = new)
        first = df[df.columns[27]]
        first = list(first)
        district = []
        def hasNumbers(inputString):
            return bool(re.search(r'\d', inputString))
        for mun in first:
            numcheck = hasNumbers(mun.split()[0])
            if numcheck == True:
                district.append(1)
            else:
                district.append(0)
        df = df.assign(district = district)
        df = df[df.district == 1]
        newname = (new + '_language_civilstatus_1980.csv')
        df.to_csv('./_language_civilstatus/' + newname)
    except:
        print('Warning!')
        break
