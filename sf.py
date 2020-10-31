from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
import pandas as pd

boston = datasets.load_boston()
features = boston.data[:, 0:3]
# print(pd.DataFrame(features))
print(features)

target = boston.target
print(len(features[:, 2]))
rf = RandomForestRegressor(random_state=0, n_jobs=1)
model = rf.fit(features, target)
# print(len(target))
print(target)
print("*" * 100)
print(model)
print(model.get_params())
