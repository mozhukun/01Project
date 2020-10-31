import pandas as pd
import os

dir = r'C:\Users\mozhukun\Desktop\数据（20201013）\落叶松数据\落叶松年轮\克一河\新数据(1950-1960)'


def sort_file_by_time(file_path):
    files = os.listdir(file_path)
    if not files:
        return
    else:
        files = sorted(files, key=lambda x: os.path.getmtime(
            os.path.join(file_path, x)))
        return files


dfs = []
filenames = sort_file_by_time(dir)
print(filenames)

for name in filenames:
    dfs.append(pd.read_excel(os.path.join(dir, name)))
    print(os.path.join(dir, name))
df = pd.concat(dfs, axis=0)
df.to_excel(r'C:\Users\mozhukun\Desktop\数据（20201013）\落叶松数据\落叶松年轮\克一河\新数据(1950-1960)\kyhTotal.xlsx', index=False)
