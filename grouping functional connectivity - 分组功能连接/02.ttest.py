# 等有时间一定改成函数形式
# 但是总感觉会被用来做非两样本t，要求在输入数据的时候注意一下
# 函数形态：ttest(data, subject, group, output)

import pandas as pd
import pingouin as pg
import numpy as np

subject = pd.read_excel('subject.xlsx', header=0)

box1 = pd.read_csv('box1.csv', header=None)
box2 = pd.read_csv('box2.csv', header=None)
box3 = pd.read_csv('box3.csv', header=None)

# 2-sample t-test
box1['group'] = subject['group']
box2['group'] = subject['group']
box3['group'] = subject['group']
# drop group 3,4 （此处是保留基线，因为是两样本t）
box1 = box1[box1['group'] < 3]
box2 = box2[box2['group'] < 3]
box3 = box3[box3['group'] < 3]


resultdf = pd.DataFrame()
# iterate over columns
for series_name, series in box1.items():
    # hc is group 1, pa is group 2
    hc = series[box1['group'] == 1]
    pa = series[box1['group'] == 2]
    # t-test
    ttest = pg.ttest(hc, pa)
    table = ttest.to_string().split()
    # combine 11st and 12nd element
    table[13] = table[13] + table[14]
    # remove 9th element
    table.pop(14)
    # add last 5 elements to result dataframe
    resultdf = pd.concat([resultdf,pd.Series(table[-8:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['T', 'dof', 'alternative', 'p-val', 'CI95%', 'cohen-d', 'BF10', 'power']
# save to csv
resultdf.to_csv('ttest-box1.csv', index=False)

resultdf = pd.DataFrame()
# iterate over columns
for series_name, series in box2.items():
    # hc is group 1, pa is group 2
    hc = series[box2['group'] == 1]
    pa = series[box2['group'] == 2]
    # t-test
    ttest = pg.ttest(hc, pa)
    table = ttest.to_string().split()
    # combine 11st and 12nd element
    table[13] = table[13] + table[14]
    # remove 9th element
    table.pop(14)
    # add last 5 elements to result dataframe
    resultdf = pd.concat([resultdf,pd.Series(table[-8:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['T', 'dof', 'alternative', 'p-val', 'CI95%', 'cohen-d', 'BF10', 'power']
# save to csv
resultdf.to_csv('ttest-box2.csv', index=False)

resultdf = pd.DataFrame()
# iterate over columns
for series_name, series in box3.items():
    # hc is group 1, pa is group 2
    hc = series[box3['group'] == 1]
    pa = series[box3['group'] == 2]
    # t-test
    ttest = pg.ttest(hc, pa)
    table = ttest.to_string().split()
    # combine 11st and 12nd element
    table[13] = table[13] + table[14]
    # remove 9th element
    table.pop(14)
    # add last 5 elements to result dataframe
    resultdf = pd.concat([resultdf,pd.Series(table[-8:])], axis=1)
# resultdf transverse
resultdf = resultdf.T
# set resultdf column name ['n', 'r', 'CI95%', 'p-val', 'roi']
resultdf.columns = ['T', 'dof', 'alternative', 'p-val', 'CI95%', 'cohen-d', 'BF10', 'power']
# save to csv
resultdf.to_csv('ttest-box3.csv', index=False)