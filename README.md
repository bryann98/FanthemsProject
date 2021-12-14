# The Fanthems Capstone Project
# CMDA majors at Virginia Tech
## Bryan Nguyen, Firaol Woldemariam, and Samhita Subramanya

## Summary
Anthem Blue Cross Blue Shield (BCBS) is a well-established health insurance company that covers millions of customers in 14 states. They would like to know the trends and patterns that have arisen over the last year due to the COVID-19 pandemic. Our team extracted the data from the Census Bureau using a web scraping script developed in Python and a relational database using AWS Relational Database Service (RDS) that automatically updates as new data is released. The data consists of approximately 2.5 million entries with 40 surveys conducted since the beginning of the pandemic, with new variables updated or removed every few weeks based on relevancy.

## Step by step process to begin working with the data
### Step 1: Run web scrape script to get files into local directory
- The web scraping script used is anthemWebScrapeTest4.py
### Step 2: Create an AWS RDS Database
- More details on Create DB.ipynb 
### Step 3: Combine all CSV Files into a single csv file
- More details on Create DB.ipynb 
### Step 4: Download MySQL Workbench or some other MySQL Client
- More details on Create DB.ipynb 
### Step 5: Use credentials and address to connect to AWS using new client
- More details on Create DB.ipynb 
### Step 6: Create Table
- More details on Create DB.ipynb 
### Step 7: Populate DB
- More details on Create DB.ipynb 
### Step 8: Use Python to connect to DB and get the data 
### Step 9: Save dataset into a csv file
### Step 10: Subset the data, rename entries and save the new dataset to a csv file
- Subseting the data is done using subset_data.ipynb
- Renaming the entries is done using rename_entries.ipynb
- The state mapping file used in the renaming step is state_map.csv
### Step 11: Upload that csv file to Tableau for visualizations
- Data used for dashboard and dashboard file (.twb and .twbx) found here:
https://drive.google.com/drive/folders/1DGb78XlECy5x6N0sANHbi0xpVVASgtTV?usp=sharing

## Updating Database
- Instructions are contained in Update_Data.ipynb

