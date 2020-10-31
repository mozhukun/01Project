import pandas as pd
import os
import numpy as np

# *
# 3—5月为春季，6—8月为夏季，9—11月为秋季，12月以及下一年的1,2月为冬季
# *


# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


# listTemp 为列表 ，n为列表的个数。注：data为1901-2019年，将1428个月份分为119个区间，每个区间12个月。
def funcSplit(listTemp, n):
    return np.array_split(listTemp, n)


inputFileDirectory = r"C:\Users\mozhukun\Desktop\数据（20201013）\落叶松数据\月均气候数据（地点分）"
outputFileDirectory = r"C:\Users\mozhukun\Desktop\data\落叶松气候数据\1950-2010"

for maindir, subdir, filenames in os.walk(inputFileDirectory):
    for filename in filenames:
        path = os.path.join(maindir, filename)
        data = pd.read_excel(path)
        outputPath = os.path.join(outputFileDirectory, filename)
        pre = list(data["pre"])
        tmp = list(data["tmp"])
        tmp2 = tmp[2:] + tmp[0:2]

        # 将1428个月份均等分为119年
        tempTmp = funcSplit(tmp, 119)
        # 将1901年1,2月放到最后再分为119份。为了计算冬季平均温度，其中最后一年冬季温度为错误数值（无最后一年的下一年1,2月份数据）。
        tempTmp2 = funcSplit(tmp2, 119)
        tempPre = funcSplit(pre, 119)

        # 各List作为存储到Excel时候的列，年份1901-2020年
        yearList = np.arange(1901, 2020)
        allyearAnnualTmpList = []
        allLastYearAnnualTmpList = []
        allGrowSeasonAnnualTmpList = []
        allSpringAnnualTmpList = []
        allSummerAnnualTmpList = []
        allAutumnAnnualTmpList = []
        allWinterAnnualTmpList = []
        allYearTotalPreList = []
        allLastYearTotalPreList = []
        allGrowSeasonTotalPreList = []

        # 树环形成当年平均温度
        for i in tempTmp:
            allyearAnnualTmpList.append(sum(i) / 12)

        # 树环形成前一年平均温度(其中第一年的前一年平均温度由所有年份平均温度代替)
        firstYearTmp_last = sum(allyearAnnualTmpList) / 119
        allLastYearAnnualTmpList = allyearAnnualTmpList[:-1]
        allLastYearAnnualTmpList.insert(0, firstYearTmp_last)

        # 当年生长季温度（5-9月）
        for i in tempTmp:
            allGrowSeasonAnnualTmpList.append(sum(i[4:9]) / 5)

        # 当年春季平均温度（3-5月）
        for i in tempTmp:
            allSpringAnnualTmpList.append(sum(i[2:5]) / 3)

        # 当年夏季平均温度（6-8月）
        for i in tempTmp:
            allSummerAnnualTmpList.append(sum(i[5:8]) / 3)

        # 当年秋季平均温度（9-11月）
        for i in tempTmp:
            allAutumnAnnualTmpList.append(sum(i[8:11]) / 3)

        # 当年冬季平均温度（12月以及下一年的1,2月）
        for i in tempTmp2:
            allWinterAnnualTmpList.append(sum(i[-3:]) / 3)

        # 树环形成当年总降水量
        for i in tempPre:
            allYearTotalPreList.append(sum(i))

        # 树环形成上一年总降水量
        allLastYearTotalPreList = allYearTotalPreList[:-1]
        firstYearPre_last = sum(allYearTotalPreList) / 119
        allLastYearTotalPreList.insert(0, firstYearPre_last)

        # # 生长季总降水（5-9月）
        for i in tempPre:
            allGrowSeasonTotalPreList.append(sum(i[4:9]))

        data_excel = {"year": yearList,
                      "yearAnnualTmp": allyearAnnualTmpList,
                      "lastYearAnnualTmp": allLastYearAnnualTmpList,
                      "growAnnualTmp": allGrowSeasonAnnualTmpList,
                      "springAnnualTmp": allSpringAnnualTmpList,
                      "summerAnnualTmp": allSummerAnnualTmpList,
                      "autumnAnnualTmp": allAutumnAnnualTmpList,
                      "winterAnnualTmp": allWinterAnnualTmpList,
                      "yearTotalPre": allYearTotalPreList,
                      "lastYearTotalPre": allLastYearTotalPreList,
                      "growSeasonTotalPre": allGrowSeasonTotalPreList}
        df = pd.DataFrame(data_excel)
        cols = ['year', 'yearAnnualTmp', 'lastYearAnnualTmp', 'growAnnualTmp',
                'springAnnualTmp', 'summerAnnualTmp', 'autumnAnnualTmp', 'winterAnnualTmp',
                "yearTotalPre", "lastYearTotalPre", "growSeasonTotalPre"]
        df = df.ix[:, cols]
        print(df)
        # 存储全部年份气候数据
        # pd.DataFrame(df).to_excel(outputPath, sheet_name='Sheet1', index=False, header=True)

        # 存储1950-2010年气候数据
        pd.DataFrame(df.loc[49:109]).to_excel(outputPath, sheet_name='Sheet1', index=False, header=True)
        print("-" * 100)
