# import os
# import xarray as xr
# import pandas as pd
# import csv
# from csv import writer
# from csv import reader
# from glob import glob
# import sys
#
# # if len(sys.argv) < 1:
# #     print('usage: DBquery.py inputPath/ outputPath/')
# #     exit(1)
# #
# # outPath = sys.argv[2]
# # inPath = sys.argv[1]
# # for item in os.listdir(inPath):
# #     if item.endswith(".nc4"):
# #
# #         data = xr.open_dataset(inPath + item)
# #         df = data.to_dataframe()
# #
# #         # df = df.dropna(axis=1, how='all')
# #
# #         output_filename = outPath + item + '.csv'
# #         df.to_csv(output_filename)
# #
# #         print(output_filename)
#
#
# # grab files
# files = glob('/home/sli/Downloads/test/*.csv')
#
#
# # simplify the file reading
# # notice this will create a generator
# # that goes through chunks of the file
# # at a time
# def read_csv(f, n=100):
#     return pd.read_csv(f, index_col=0, chunksize=n)
#
#
# # simplify the concatenation
# def concat(lotX):
#     return pd.concat(lotX, axis=0)
#
#
# # simplify the writing
# # make sure mode is append and header is off
# # if file already exists
# def to_csv(f, df):
#     if os.path.exists(f):
#         mode = 'a'
#         header = False
#     else:
#         mode = 'w'
#         header = True
#     df.to_csv(f, mode=mode, header=header)
#
#
# # Fun stuff! zip will take the next element of the generator
# # for each generator created for each file
# # concat one chunk at a time and write
# for lot in zip(*[read_csv(f, n=10) for f in files]):
#     to_csv('/home/sli/Downloads/test/out.csv', concat(lot))

import pandas as pd
import glob

path = '/home/sli/Downloads/test/' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=0)
    li.append(df)

frame = pd.concat(li, axis=0)
frame.to_csv('/home/sli/Downloads/output1.csv')
