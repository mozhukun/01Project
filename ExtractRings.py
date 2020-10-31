import re
import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

widthList = []
nameyearList = []
allNameList = []
lineList = []
yearList = []

openExcel = r"E:\test2\txt\漠河.txt"

writeExcel = r'E:\test2\漠河\mh64.xlsx'
with open(openExcel, "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        treeNumber = line[0:5]
        # print(treeNumber)
        treeNumber = treeNumber.strip()
        # treeNumber = treeNumber[-2:]
        if treeNumber == 'mh64':
            line = line.split()
            widthLine = line[2:]
            for i in widthLine:
                widthList.append(i)
            yearList.append(line[1])
print(treeNumber)

id = ['64'] * len(widthList)
print(widthList)
firstYear = yearList[0]
yearList2 = []
for year in range(int(firstYear), int(firstYear) + len(widthList)):
    yearList2.append(str(year))
print(yearList2)

ageList = []
for i in range(1, 1 + len(widthList)):
    ageList.append(i)
R = []
sum = 0
for i in widthList:
    sum = sum + float(i)
    R.append(sum / 10000)
print(widthList)
print('R: ', R)
R2 = R[0:len(R) - 1]
R2.insert(0, 0)
print('R2:', R2)

v = list(map(lambda x: 3.14 * (x[0] * x[0] - x[1] * x[1]), zip(R, R2)))
BAI = np.array(v)

data = {'ID': id, 'year': yearList2, 'age': ageList, 'width': widthList, 'R(cm)': R, "BAI": BAI}
df = pd.DataFrame(data)
pd.DataFrame(df).to_excel(writeExcel, sheet_name='Sheet1', index=False, header=True)

print('id:', len(id))
print('year:', len(yearList))
print('age:', len(ageList))
print('width:', len(widthList))
