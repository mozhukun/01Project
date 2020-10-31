from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
import collections
from sklearn import svm

pd.set_option('expand_frame_repr', False)
np.set_printoptions(suppress=True)
pd.set_option('display.max_rows', None)
df1 = pd.read_excel(r'E:\test\fenlei7_Train.xlsx')
data_features = df1[['blue', 'green', 'nir', 'red', 'NDVI', 'GNDVI', 'LCI', 'NDRE',
                     'elev_min', 'elev_percentile_99th',
                     'density_metrics[6]', 'density_metrics[8]', 'int_cv', 'int_max', 'int_skewness',
                     'Area']]
data_classifier = df1['TreeType']
X = np.array(data_features)
y = np.array(data_classifier)
# # np.random.seed(50)#随机种子
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=df1['TreeType'], random_state=1)
print('=' * 100)
print('训练数据个数:', len(y_train))
print('测试数据个数:', len(y_test))
print('=' * 100)
train = collections.Counter(y_train)
print('每层抽样个数如下:')
print(train.most_common())
print('=' * 100)
blueList = []
indexList = []
FIDList = []
for i in range(1, int(len(X_test) + 1)):
    a = X_test[i - 1]
    blueList.append(a[0])
print('Test数据中特征“blue”对应的数据：', blueList)
for i in blueList:
    indexa = df1[(df1.blue == i)].index
    indexList.append(indexa)
print('==' * 200)
for i in indexList:
    aaa = df1.loc[i[0]]
    FIDList.append(aaa[0])
print('Test数据的FID：', FIDList)
print('=' * 200)

# x_train真实训练，x_test真实检验，y_train预测训练，y_test预测检验
classifier = svm.SVC(kernel='linear', C=100)
classifier.fit(X_train, y_train)
y_train_pred = classifier.predict(X_train)
y_test_pred = classifier.predict(X_test)
print('训练数据得分：%s' % accuracy_score(y_train, y_train_pred))
print('测试数据得分：%s' % accuracy_score(y_test, y_test_pred))
#
data_train = {'训练真实数据': y_train, '训练预测数据': y_train_pred}
df2 = pd.DataFrame(data_train)
pd.DataFrame(df2).to_excel(r'E:\test\data_train.xlsx', sheet_name='Sheet1', index=False, header=True)

data_test = {'测试真实数据': y_test, '测试预测数据': y_test_pred, 'blue': blueList, 'FID': FIDList}
df3 = pd.DataFrame(data_test)
pd.DataFrame(df3).to_excel(r'E:\test\data_test.xlsx', sheet_name='Sheet1', index=False, header=True)

df_pred = pd.read_excel(r'E:\test\fenlei7_PredictData.xlsx')
dataPred_features = df_pred[['blue', 'green', 'nir', 'red', 'NDVI', 'GNDVI', 'LCI', 'NDRE',
                             'elev_min', 'elev_percentile_99th',
                             'density_metrics[6]', 'density_metrics[8]', 'int_cv', 'int_max', 'int_skewness',
                             'Area']]
y_pred_pred = classifier.predict(dataPred_features)
df_pred['TreeType'] = y_pred_pred
df_aaa = pd.DataFrame(df_pred)
pd.DataFrame(df_aaa).to_excel(r'E:\test\fenlei7_PredictData_type.xlsx', sheet_name='Sheet1', index=False, header=True)
