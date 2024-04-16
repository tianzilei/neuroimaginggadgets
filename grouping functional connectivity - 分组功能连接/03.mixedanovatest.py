# 等有时间一定改成函数形式
# 函数形态：mixed_anova_test(data, between, within, subject, savepath)

import pandas as pd
import pingouin as pg
import numpy as np

subject = pd.read_excel('subject(anova).xlsx', header=0)

box1 = pd.read_csv('box1.csv', header=None)
box2 = pd.read_csv('box2.csv', header=None)
box3 = pd.read_csv('box3.csv', header=None)
box1 = box1[subject['type'] != 1]
box2 = box2[subject['type'] != 1]
box3 = box3[subject['type'] != 1]
subject = subject[subject['type'] != 1]

resultdf = pd.DataFrame()
for series_name, series in box1.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    mixed = pg.mixed_anova(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    table = mixed.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[10:19])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[20:29])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[30:39])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Source', 'SS', 'DF1', 'DF2', 'MS', 'F', 'p-unc', 'np2', 'eps']
# save to csv
resultdf.to_csv('mixed-box1.csv', index=False)

resultdf = pd.DataFrame()
for series_name, series in box2.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    mixed = pg.mixed_anova(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    table = mixed.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[10:19])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[20:29])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[30:39])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Source', 'SS', 'DF1', 'DF2', 'MS', 'F', 'p-unc', 'np2', 'eps']
# save to csv
resultdf.to_csv('mixed-box2.csv', index=False)

resultdf = pd.DataFrame()
for series_name, series in box3.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    mixed = pg.mixed_anova(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    table = mixed.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[10:19])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[20:29])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[30:39])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Source', 'SS', 'DF1', 'DF2', 'MS', 'F', 'p-unc', 'np2', 'eps']
# save to csv
resultdf.to_csv('mixed-box3.csv', index=False)