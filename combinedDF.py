# import numpy
import os
# from io import BytesIO
# from zipfile import ZipFile
import glob
import pandas as pd
import datetime
import fnmatch
import csv
from datetime import datetime, timedelta
dirpath = r'C:\Users\thela\Downloads\AntWebScrape' # Change to desired directory
os.chdir(dirpath)
csv_list = []
# Convert current time to seconds
currDate = datetime.today() 
currSec = currDate.timestamp()
# For each csv file in directory containing raw data  
for file_name in glob.glob(os.path.join(dirpath, '*.csv')):
    if fnmatch.fnmatch(file_name, '*puf*') and not "repwgt" in file_name:
        # Get time the file was modified
        fileSec = os.path.getmtime(file_name)
        diffTime = currSec - fileSec
        # If file was modified within last 24 hours
        if diffTime <= 86400:
            print(file_name)
        # Add file name to list of csv files
        csv_list.append(file_name)

# If directory does not exist yet, make it
comPath = r'C:\Users\thela\Downloads\AntWebScrapeCombined' # Change to desired directory
if not os.path.exists(comPath): 
     os.makedirs(comPath)

# If the dataset for each phase does not exist, make it and store into dataframe
from itertools import chain
os.chdir(comPath)
comb1 = r'C:\Users\thela\Downloads\AntWebScrapeCombined\combined_1.csv' # Change to appropiate file path
comb2 = r'C:\Users\thela\Downloads\AntWebScrapeCombined\combined_2.csv'
comb3 = r'C:\Users\thela\Downloads\AntWebScrapeCombined\combined_3.csv'
comb31 = r'C:\Users\thela\Downloads\AntWebScrapeCombined\combined_31.csv'
comb32 = r'C:\Users\thela\Downloads\AntWebScrapeCombined\combined_32.csv'
if not os.path.exists(comb1):
    csv_phase1 = list(chain(csv_list[0:11]))
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_phase1 ])
    combined_csv.to_csv( "combined_1.csv", index=False, encoding='utf-8-sig')

if not os.path.exists(comb2):
    csv_phase2 = list(chain(csv_list[12:16]))
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_phase2 ])
    combined_csv.to_csv( "combined_2.csv", index=False, encoding='utf-8-sig')

if not os.path.exists(comb3):
    csv_phase3 = list(chain(csv_list[17:26]))
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_phase3 ])
    combined_csv.to_csv( "combined_3.csv", index=False, encoding='utf-8-sig')

if not os.path.exists(comb31):
    csv_phase31 = list(chain(csv_list[27:32]))
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_phase31 ])
    combined_csv.to_csv( "combined_31.csv", index=False, encoding='utf-8-sig')

if not os.path.exists(comb32):
    csv_phase32 = list(chain(csv_list[33:38]))
    combined_csv = pd.concat([pd.read_csv(f) for f in csv_phase32 ])
    combined_csv.to_csv( "combined_32.csv", index=False, encoding='utf-8-sig')

df1 = pd.read_csv("combined_1.csv") 
df2 = pd.read_csv("combined_2.csv") 
df3 = pd.read_csv("combined_3.csv") 
df31 = pd.read_csv("combined_31.csv") 
df32 = pd.read_csv("combined_32.csv")
