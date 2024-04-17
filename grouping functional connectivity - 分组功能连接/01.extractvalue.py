# 等有时间一定改成函数形式
# 函数形态：输入组内roi数量（eg:96, 22, 24），矩阵（'rsub_'），输出对应数量csv

import os, shutil
import pandas as pd

dir = r'path\to\dir'

def createtxt(txtname):
    if os.path.exists(txtname):
        os.remove(txtname)
    with open(txtname, 'w') as f:
        f.write('')
    return txtname

txt1 = createtxt('box1.csv')
txt2 = createtxt('box2.csv')
txt3 = createtxt('box3.csv')

import numpy as np
import scipy.stats as stats

# flatten the 2-D array to 1-D array
def flatten(array):
    array = array.flatten()
    array = array.tolist()
    array = str(array).replace('[', '').replace(']', '')
    return array

# for text start with 'rsub_'(from gretna)
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.startswith('zsub_'):
            df = pd.read_csv(os.path.join(root, file), sep='\t', header=None)
            # drop the last column
            # if the last column is not the label, please change the number
            df.drop(df.columns[-1], axis=1, inplace=True)

            # 这个地方需要注意的是：
            # 1. python中的list是从0开始的，所以range(0, 96)表示的是第0到第95列
            # 2. Python左闭右开，所以range(0, 96)表示的是第0到第95列

            # lt(left top), rb(right bottom)
            # box = df.iloc[lty:rby, ltx:rbx]
            box1 = df.iloc[96:112, 0:96]
            box2 = df.iloc[112:, 0:96]
            box3 = df.iloc[112:, 96:112]

            box1 = flatten(box1.to_numpy())
            box2 = flatten(box2.to_numpy())
            box3 = flatten(box3.to_numpy())

            with open(txt1, 'a') as f:
                f.write(box1 + '\n')
            with open(txt2, 'a') as f:
                f.write(box2 + '\n')
            with open(txt3, 'a') as f:
                f.write(box3 + '\n')