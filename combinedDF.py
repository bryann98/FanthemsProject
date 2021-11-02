# import bs4
import zipfile
import requests
# import numpy
# import pandas as pd
import os
import pickle
# from io import BytesIO
# from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

# If directory does not exist yet, make it
comPath = r'C:\Users\thela\Downloads\AntWebScrapeCombined' # Change to desired directory
if not os.path.exists(comPath): 
     os.makedirs(comPath)

import fnmatch
csv_list = []
for file_name  in glob.glob(os.path.join(dirpath, '*.csv')):
    if fnmatch.fnmatch(file_name, '*puf*') and not "repwgt" in file_name:
        csv_list.append(file_name)
os.chdir(comPath)
#combined_csv = pd.concat([pd.read_csv(f) for f in csv_list ])
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

import csv
fieldnames = []
# First determine the field names from the top line of each input file
for filename in csv_list:
  with open(filename, "r", newline="") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        fieldnames.append(h)

# Then copy the data
with open("out.csv", "w", newline="") as f_out:
  writer = csv.DictWriter(f_out, fieldnames=fieldnames)
  for filename in csv_list:
    with open(filename, "r", newline="") as f_in:
        # Uses the field names in this file
        reader = csv.DictReader(f_in)  
        for line in reader:
            writer.writerow(line)

df = pd.read_csv ('out.csv')
print(df)