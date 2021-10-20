# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:13:34 2021

@author: thela
"""
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

# Create directories for storage
dirpath = r'C:\Users\thela\Downloads\AntWebScrape' # Change to desired directory
listpath = r'C:\Users\thela\Downloads\curr_list.txt' # List of links
if not os.path.exists(dirpath): # If directory does not exist yet, make it
    os.makedirs(dirpath)

# If list does not exist yet, make it
try:
    with open(listpath, 'rb') as f:
        curr_List = pickle.load(f)
except IOError:
    curr_List = []
    
# Open website    
page = urlopen("https://www.census.gov/programs-surveys/household-pulse-survey/datasets.html")
soup = BeautifulSoup(page, 'html.parser')

# Identify url links of required zip files
zipfile_urls = soup.select("a[href$='CSV.zip']")
links = [link.get('href') for link in zipfile_urls]
zipLinks = ["http:" + s for s in links]

# Get difference between website list and current list
diff = list(set(zipLinks) - set(curr_List))

# Extract necessary zip content to directory
import io
for i in diff:
    r = requests.get(i)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dirpath)

# Update current list of zip files and store in txt file
new_List = zipLinks
with open(listpath, 'wb') as f:
    pickle.dump(new_List, f)

# # Open database connection with MySQL Database
# import MySQLdb
# import pymysql
# h = config.get('mysql','host')
# u = config.get('mysql','user')
# pt = config.get('mysql', 'port')
# pw = config.get('mysql','password')
# db = config.get('mysql','db')
# sql_db = MySQLdb.connect(h,pt,u,pw,db)

# cursor = sql_db.cursor()
# cursor.execute("DROP TABLE IF EXISTS")
# sql = """LOAD DATA LOCAL INFILE '{}'
# INTO TABLE system_work
# FIELDS TERMINATED BY ','
# OPTIONALLY ENCLOSED BY '"'
# LINES TERMINATED BY '\\r\\n'
# IGNORE 1 LINES;;"""

# currFiles = os.listdir(dirpath)
# import fnmatch
# for file_name in currFiles:
#     if fnmatch.fnmatch(file_name, '*puf*'):
#         try:
#             cursor = sql_db.cursor()
#             cursor.execute(sql.format(file_name))
#             sql_db.commit()
#         except Exception:
#             # Rollback in case there is any error
#             sql_db.rollback()
#         try:
#             # Execute the SQL command and commit your changes in the database
#             cursor.execute(sql)
#             sql_db.commit()
#         except:
#             sql_db.rollback()

# # disconnect from server
# sql_db.close()

import glob
import os
import datetime
from datetime import datetime, timedelta
currDate = datetime.today()
currSec = currDate.timestamp() # Convert current time to seconds
for file_name in glob.glob(os.path.join(dirpath, '*.csv')):
    fileSec = os.path.getmtime(file_name)
    diffTime = currSec - fileSec
    if diffTime <= 86400:
        print(file_name)