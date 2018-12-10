import urllib.request, urllib.parse, urllib.error
import tabula
from tabula import read_pdf
import glob, os
import pandas as pd
import re

links = [
#1980:
#BE:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345654/master",
#VS:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345684/master",
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
#GR:
"https://www.bfs.admin.ch/bfsstatic/dam/assets/345658/master"
]

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
        def redcol(inputdf):
            return bool(re.search(r'Unnamed', inputdf))
        # First dataframe (Swiss and foreign population):
        # For Fribourg (FR), Bern (BE), Valais (VS) and Graubünden (GR):
        if i == '345656' or i == '345654' or i == '345684' or i == '345658':
            df = read_pdf(name, pages="26", area=(118.64,55.25,718.41,505.21))
            df2 = read_pdf(name, pages="28", area=(118.64,55.25,718.41,505.21))
            df2.loc[len(df2.index)] = df2.columns
            for two in list(df2.columns):
                namecheck = redcol(two)
                if namecheck == True:
                    df2 = df2.drop(two, axis=1)
            print('TWO')
            print(len(df2.columns))
            for two in range(0, len(df2.columns)):
                df2 = df2.rename(index=str, columns={df2.columns[two]:df.columns[two]})
            df3 = read_pdf(name, pages="30", area=(118.64,55.25,718.41,505.21))
            df3.loc[len(df3.index)] = df3.columns
            for two in list(df3.columns):
                namecheck = redcol(two)
                if namecheck == True:
                    df3 = df3.drop(two, axis=1)
            print('THREE')
            print(len(df3.columns))
            for j in range(0, len(df3.columns)):
                df3 = df3.rename(index=str, columns={df3.columns[j]:df.columns[j]})
            df = df.append([df2,df3], sort=False)
            # For Fribourg (FR), Bern (BE) and Graubünden (GR):
            if i == '345656' or i == '345654' or i == '345658':
                df4 = read_pdf(name, pages="32", area=(118.64,55.25,718.41,505.21))
                df4.loc[len(df4.index)] = df4.columns
                for two in list(df4.columns):
                    namecheck = redcol(two)
                    if namecheck == True:
                        df4 = df4.drop(two, axis=1)
                print('FOUR')
                print(len(df4.columns))
                for j in range(0, len(df4.columns)):
                    df4 = df4.rename(index=str, columns={df4.columns[j]:df.columns[j]})
                df5 = read_pdf(name, pages="34", area=(118.64,55.25,718.41,505.21))
                df5.loc[len(df5.index)] = df5.columns
                for two in list(df5.columns):
                    namecheck = redcol(two)
                    if namecheck == True:
                        df5 = df5.drop(two, axis=1)
                print('FIVE')
                print(len(df5.columns))
                for j in range(0, len(df5.columns)):
                    df5 = df5.rename(index=str, columns={df5.columns[j]:df.columns[j]})
                df = df.append([df4,df5], sort=False)
                #For Valais (VS) and Bern (BE):
                if i == '345690' or i == '345654':
                    df6 = read_pdf(name, pages="36", area=(118.64,55.25,718.41,505.21))
                    df6.loc[len(df6.index)] = df6.columns
                    for two in list(df6.columns):
                        namecheck = redcol(two)
                        if namecheck == True:
                            df6 = df6.drop(two, axis=1)
                    for j in range(0, len(df6.columns)):
                        df6 = df6.rename(index=str, columns={df6.columns[j]:df.columns[j]})
                    df = df.append(df6, sort=False)
                    print(df)
                    #For Bern (BE):
                    if i == '345654':
                        df7 = read_pdf(name, pages="38", area=(118.64,55.25,718.41,505.21))
                        df7.loc[len(df7.index)] = df7.columns
                        for two in list(df7.columns):
                            namecheck = redcol(two)
                            if namecheck == True:
                                df7 = df7.drop(two, axis=1)
                        for j in range(0, len(df7.columns)):
                            df7 = df7.rename(index=str, columns={df7.columns[j]:df.columns[j]})
                        df = df.append(df7, sort=False)
        # For all others:
        else:
            df = read_pdf(name, pages="19",area=(118.64,55.25,718.41,505.21))
            # For Zurich (ZH), Basel-Landschaft (BL) and St. Gallen (SG):
            if i == '345690' or i == '345650' or i == '345670':
                df2 = read_pdf(name, pages="21",area=(118.64,55.25,718.41,505.21))
                df2.loc[len(df2.index)] = df2.columns
                for j in range(0, len(df2.columns)):
                    df2 = df2.rename(index=str, columns={df2.columns[j]:df.columns[j]})
                df = df.append(df2, sort=False)
                #For Zurich (ZH):
                if i == '345690':
                    df3 = read_pdf(name, pages="23",area=(118.64,55.25,718.41,505.21))
                    df3.loc[len(df3.index)] = df3.columns
                    for j in range(0, len(df3.columns)):
                        df3 = df3.rename(index=str, columns={df3.columns[j]:df.columns[j]})
                    df = df.append(df3, sort=False)
        new = df.columns.values[0]
        new = new.split()
        print(new)
        # For Fribourg (FR) and Valais (VS):
        if i == '345684' or i == '345656':
            new = new[2]
        # For Appenzell Innerhoden (AI) and Ausserhoden (AR):
        elif i == '345648' or i == '345646':
            new = (new[1] + '_' + new[2])
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
        # For Uri (UR) and St. Gallen (SG):
        if i == '345682' or i == '345670':
            df = df.drop('Unnamed: 1', axis=1)
            df.columns = varnames[0:12]
        # For all others:
        else:
            df.columns = varnames[0:12]
        # Assign canton-level variables:
        df = df.assign(can_name = new)
        df = df.assign(can_population = canton[1])
        for j in range(2,len(canton)):
            df = df.assign(varname = canton[j])
            varnew = ('can_' + varnames[j])
            df.rename(columns={"varname": varnew}, inplace=True)
        first = df[df.columns[0]]
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
        newname = (new + '_population_1980.csv')
        df.to_csv('./_population/' + newname)
    except:
        print('Warning!')
        break
