import urllib.request, urllib.parse, urllib.error
import tabula
from tabula import read_pdf
import glob, os
import pandas as pd
import re

links = [
#1980:
#AG:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345644/master",
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
        # Fourth dataframe (Employment):
        # For Bern (BE):
        if i == '345654':
            df1 = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="57", area=(131.18,35.66,702.1,494.57))
        # For Valais (VS):
        elif i == '345684':
            df1 = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="41", area=(131.18,35.66,702.1,494.57))
        # For Fribourg (FR) and Graubünden (GR):
        elif i == '345656' or i == '345658':
            df1 = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="49", area=(131.18,35.66,702.1,494.57))
        # For Aargau (AG) and Thurgau (TG):
        elif i == '345644' or i == '345678':
            df1 = read_pdf(name, pages="19", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="38", area=(131.18,35.66,702.1,494.57))
        # For Solothurn (SO) and Zurich (ZH):
        elif i == '345676' or i == '345690':
            df1 = read_pdf(name, pages="19", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="34", area=(131.18,35.66,702.1,494.57))
        # For Luzern (LU), Basel-Landschaft (BL) and St. Gallen (SG):
        elif i == '345662' or i == '345670' or i == '345650':
            df1 = read_pdf(name, pages="19", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="30", area=(131.18,35.66,702.1,494.57))
        # For all others:
        else:
            df1 = read_pdf(name, pages="19", area=(118.64,55.25,718.41,505.21))
            df = read_pdf(name, pages="26",area=(131.18,35.66,702.1,494.57))
        new = df1.columns.values[0]
        new = new.split()
        # For Fribourg (FR) and Valais (VS):
        if i == '345656' or i == '345684':
            new = new[2]
        # For Zug (ZG):
        elif i == '345688':
            new = 'ZUG'
        # For all others:
        else:
            new = new[1]
        print(new)
        for name in glob.iglob(name):
            os.rename(name, (new + '_1980.pdf'))
        canton = list(df.columns.values)
        print(canton)
        # For Basel-Landschaft (BL):
        if i == '345650':
            df = df.drop('Unnamed: 7', axis=1)
            df.columns = varnames[58:71]
        # For Thurgau (TG):
        if i == '345678':
            df = df.drop('Unnamed: 1', axis=1)
            df.columns = varnames[58:71]
        # For Solothurn (SO):
        if i == '345676':
            df.columns = varnames[58:70]
        # For all others:
        else:
            df.columns = varnames[58:71]
        # Assign canton-level variables:
        df = df.assign(can_name = new, can_employed = canton[1])
        for j in range(2,len(canton)):
            df = df.assign(varname = canton[j])
            varnew = ('can_' + varnames[(j+58)])
            df.rename(columns={"varname": varnew}, inplace=True)
        first = df[df.columns[0]]
        first = list(first)
        print(first)
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
        newname = (new + '_employment_1980.csv')
        df.to_csv('./_employment/' + newname)
    except:
        print('Warning!')
        break
