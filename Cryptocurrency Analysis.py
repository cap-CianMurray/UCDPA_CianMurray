# Certificate in Data Analytics for Finance
# Cian Murray cian.murray@capspire.com
# 15/04/2021
# Datasets Urls:
# https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory
# https://datahub.io/core/gold-prices
# camelCase will be used as a coding standard throughout.
# numpy will be used for creating arrays and Algebra
# pandas to be used for importing of data and data manipulation.
# matplotlib and seaborn to be used for data visualisation


import numpy as np
import pandas as pd
desired_width=400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)
import matplotlib.pyplot as plt
import seaborn as sns
colour = sns.color_palette()

# I created a data seperator in order to make it easier to visualise sections within the project.
# I will not be using this as my defined function, It is solely used for finding returned data quickly.

colourRed = '\033[0;31m'  # Red Seperator
revertColour = '\033[0;30m'  # We now revert the ANSI formatting otherwise it will stay as Red throughout.
dataSeperator = colourRed + "\n" * 3 + '*' * 113 + "\n"*3 + revertColour

# Import our gold historical data and look at the head
goldDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\gold_monthly_csv.csv')
print ("Gold Dataframe :\n",goldDf.head(),dataSeperator)

# Import our Cryptocurrency historical coin data and look at the head
cryptoDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\coin_Bitcoin.csv')
print ("Bitcoin Dataframe :\n",cryptoDf.head(),dataSeperator)


# Section 1 Data Cleanup of goldDf


# Inspect the dataframe
print(goldDf.info())
print(goldDf.shape)
print(goldDf.describe())
print(goldDf.columns,dataSeperator)

# Change the date to European Format
goldDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')

#Insert a new column that shows name of the asset we are using , in this case Gold
goldDf.insert(0, "Name", "Gold")

# Summary statistics for goldDf
goldMinD = goldDf["Date"].min()
goldMaxD = goldDf["Date"].max()
print("Gold Minimum date: ",goldMinD)
print("Gold Maximum date: ",goldMaxD)
print("Gold Median Price: ",goldDf["Price"].median())
print("Gold Minimum Price: ",goldDf["Price"].min())
print("Gold Maximum Price: ",goldDf["Price"].max())
print("Gold Var: ",goldDf["Price"].var())
print("Gold Standard deviation: ",goldDf["Price"].std(),dataSeperator)


# Check for any Null Values in the Data
nullValues2 = 0
nullValues = goldDf.isna().sum().sum()
print("There are: ",nullValues," Null values in the Dataset",dataSeperator)


# In commodity Trading we refer to the closing price as the settlement price for several reasons.
# I will rename the price column to this as it will be easier for colleagues to follow the data.
goldDf.rename(columns = {'Price': 'Settlement'}, inplace = True)
print(goldDf.head(),dataSeperator)


# Section 2 Data Cleanup of cryptoDf

# Inspect the dataframe
print(cryptoDf.info())
print(cryptoDf.shape)
print(cryptoDf.describe())
print(cryptoDf.columns,dataSeperator)

nullValues2 = 0
nullValues = goldDf.isna().sum().sum()
print("There are: ",nullValues," Null values in the Dataset",dataSeperator)


# Rename Closing price to Settlement
cryptoDf.rename(columns = {'Close': 'Settlement'}, inplace = True)
print(cryptoDf.head(),dataSeperator)

# Create new dataframes for analysis between Bitcoin and Gold with the columns we require
cryptoDf2 = cryptoDf[['Name', 'Date', 'Settlement']].copy()
goldDf2 = goldDf[['Name', 'Date', 'Settlement']].copy()
print(cryptoDf2.head(),dataSeperator)

# Change the date to European Format
cryptoDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')
print(cryptoDf.head(),dataSeperator)

# # Change the Date columns from Float to datetime object.
# goldDf2["Date"] = pd.to_datetime(goldDf2["Date"])
# cryptoDf2["Date"] = pd.to_datetime(cryptoDf2["Date"])
# dataType = goldDf2.dtypes, cryptoDf2.dtypes
# print('Data types for each dataframe :',dataType,dataSeperator)

goldMinD = goldDf["Date"].min()
goldMaxD = goldDf["Date"].max()
bitCoinMinD = cryptoDf2["Date"].min()
bitCoinMaxD = cryptoDf2["Date"].max()
print("Gold Minimum Date: ",goldMinD," Bitcoin Minimum Date: ",bitCoinMinD )
print("Gold Maximum Date: ",goldMaxD," Bitcoin Maximum Date: ",bitCoinMaxD )

print(goldDf2.head())
print (cryptoDf2.head(),dataSeperator)





# The data in the cryptoDf2 is grouped by day where as goldDf2 is grouped by month, now we group and sum the
# goldDf2 Date column in order to bring it in line with that of cryptoDf2.


