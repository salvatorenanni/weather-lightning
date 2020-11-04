import os
import xarray as xr
import pandas as pd
import csv
from csv import writer
from csv import reader
from glob import glob
import numpy as np
import sys


def filters(df, elem):
    tmp = df.loc[df['light'] > 0]
    app_data = []
    cx = -1
    cy = -1
    for i in range(len(tmp)):
        cx = tmp.values[i][38]
        cy = tmp.values[i][39]

        data = df[(df.X - cx) ** 2 + (df.Y - cy) ** 2 < r ** 2]
        app_data.append(data)

    if cx != -1 and cy != -1:
        app_data = pd.concat(app_data).drop_duplicates(keep='first')
        app_data.to_csv(outPath + elem, index=False)


if len(sys.argv) < 2:
    print('usage: circle.py inputPath/ outputPath/ circleSize')
    exit(1)

outPath = sys.argv[2]
inPath = sys.argv[1]
r = sys.argv[3]

for item in os.listdir(inPath):
    if item.endswith(".csv"):
        df1 = pd.read_csv(inPath + item)
        print(item)
        filters(df1, item)

# item = '/home/sli/Downloads/csv/wrf5_d03_20200801Z1500.nc.nc4.csv'

# df.drop_duplicates()


# def filters(df):
#     tmp = df.loc[df['light'] > 0]
#     # appended_data = pd
#
#     for i in range(len(tmp)):
#         cx = -1
#         cy = -1
#         cx = tmp.values[i][38]
#         cy = tmp.values[i][39]
#
#         if i == 0:
#             appended_data = df[(df.X - cx) ** 2 + (df.Y - cy) ** 2 < r ** 2]
#         else:
#             pd.concat([appended_data, df[(df.X - cx) ** 2 + (df.Y - cy) ** 2 < r ** 2]], ignore_index=True)
#
#     # appended_data = pd.concat(appended_data)
#         if cx != -1 and cy != -1:
#             # appended_data.drop_duplicates()
#             appended_data.to_csv(outPath + item)
#
#
# for item in os.listdir(inPath):
#     if item.endswith(".csv"):
#         df1 = pd.read_csv(inPath + item)
#         print(item)
#         filters(df1)

# Nump = df[['X', 'Y']].to_numpy()
# coords = tmp[['X', 'Y']].to_numpy()
#
# # for item in coords:
# #     for elem in Nump:
#
# df1 = np.where(((x[:]-cx[:])**2 + (y[:]-cy[:])**2) < r**2)
#
# for i in range(len(df1[1])):
#     print(str(df1[0][i]) + '\t' + str(df1[1][i]))

# print(df1[0][:])
# print('\t')
# print (df1[1][:])


# mask = (x[np.newaxis,:]-cx)**2 + (y[:,np.newaxis]-cy)**2 < r**2
