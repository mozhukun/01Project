import pandas as pd
import os

for maindir, subdir, filenames in os.walk(r"E:\test2\漠河"):
    for filename in filenames:
        path = os.path.join(maindir, filename)
        print(path)
        portion = os.path.splitext(path)
        path2 = r"E:\test3\漠河"
        path3 = os.path.join(path2, filename)
        # print(path3)
        data = pd.read_excel(path)
        # print(maindir)
        # print(data[:-1])
        df = pd.DataFrame(data[:-1])
        pd.DataFrame(df).to_excel(path3, sheet_name='Sheet1', index=False, header=True)
        print(df)
        print("*" * 100)
