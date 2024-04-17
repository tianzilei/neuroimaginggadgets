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
resultdfc = pd.DataFrame()
resultdfe = pd.DataFrame()
for series_name, series in box1.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    pairwise = pg.pairwise_tests(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    pttestc = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='taichi'])
    ptteste = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='exercise'])
    table = pairwise.to_string().split()
    table[39] = table[39] + table[40] + table[41]
    table.pop(40)
    table.pop(41)
    table[54] = table[54] + table[55] + table[56]
    table.pop(55)
    table.pop(56)
    tablec = pttestc.to_string().split()
    tablee = ptteste.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[13:25])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[26:38])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[39:51])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[52:])], axis=1)
    resultdfc = pd.concat([resultdfc,pd.Series(tablec[12:])], axis=1)
    resultdfe = pd.concat([resultdfe,pd.Series(tablee[12:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
resultdfc = resultdfc.T
resultdfe = resultdfe.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Contrast', 'Time', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfc.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfe.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
# save to csv
resultdf.to_csv('pairwise-box1.csv', index=False)
resultdfc.to_csv('pttest-taichi-box1.csv', index=False)
resultdfe.to_csv('pttest-exercise-box1.csv', index=False)

resultdf = pd.DataFrame()
resultdfc = pd.DataFrame()
resultdfe = pd.DataFrame()
for series_name, series in box2.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    pairwise = pg.pairwise_tests(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    pttestc = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='taichi'])
    ptteste = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='exercise'])
    table = pairwise.to_string().split()
    table[39] = table[39] + table[40] + table[41]
    table.pop(40)
    table.pop(41)
    table[54] = table[54] + table[55] + table[56]
    table.pop(55)
    table.pop(56)
    tablec = pttestc.to_string().split()
    tablee = ptteste.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[13:25])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[26:38])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[39:51])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[52:])], axis=1)
    resultdfc = pd.concat([resultdfc,pd.Series(tablec[12:])], axis=1)
    resultdfe = pd.concat([resultdfe,pd.Series(tablee[12:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
resultdfc = resultdfc.T
resultdfe = resultdfe.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Contrast', 'Time', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfc.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfe.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
# save to csv
resultdf.to_csv('pairwise-box2.csv', index=False)
resultdfc.to_csv('pttest-taichi-box2.csv', index=False)
resultdfe.to_csv('pttest-exercise-box2.csv', index=False)

resultdf = pd.DataFrame()
resultdfc = pd.DataFrame()
resultdfe = pd.DataFrame()
for series_name, series in box3.items():
    newdf = series.to_frame()
    # dataframe name 'fc'
    newdf.columns = ['fc']
    # replace zero with average
    newdf = newdf.replace(0, np.nan)
    newdf = newdf.fillna(newdf.mean())
    newdf = pd.concat([newdf, subject], axis=1)
    pairwise = pg.pairwise_tests(dv='fc', between='Group', within='Time', subject='Subject', data=newdf)
    pttestc = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='taichi'])
    ptteste = pg.pairwise_tests(dv='fc', within='Time', subject='Subject', data=newdf[newdf['Group']=='exercise'])
    table = pairwise.to_string().split()
    table[39] = table[39] + table[40] + table[41]
    table.pop(40)
    table.pop(41)
    table[54] = table[54] + table[55] + table[56]
    table.pop(55)
    table.pop(56)
    tablec = pttestc.to_string().split()
    tablee = ptteste.to_string().split()
    resultdf = pd.concat([resultdf,pd.Series(table[13:25])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[26:38])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[39:51])], axis=1)
    resultdf = pd.concat([resultdf,pd.Series(table[52:])], axis=1)
    resultdfc = pd.concat([resultdfc,pd.Series(tablec[12:])], axis=1)
    resultdfe = pd.concat([resultdfe,pd.Series(tablee[12:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
resultdfc = resultdfc.T
resultdfe = resultdfe.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['Contrast', 'Time', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfc.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
resultdfe.columns = ['Contrast', 'A', 'B', 'Paired', 'Parametric', 'T', 'dof', 'alternative', 'p-unc', 'BF10', 'hedges']
# save to csv
resultdf.to_csv('pairwise-box3.csv', index=False)
resultdfc.to_csv('pttest-taichi-box3.csv', index=False)
resultdfe.to_csv('pttest-exercise-box3.csv', index=False)