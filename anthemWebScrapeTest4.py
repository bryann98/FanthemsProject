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
url = "https://www.census.gov/programs-surveys/household-pulse-survey/datasets.html"   
page = urlopen(url)
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
