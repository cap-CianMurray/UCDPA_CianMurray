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
import matplotlib.pyplot as plt
import seaborn as sns
colour = sns.color_palette()

# I created a data seperator in order to make it easier to visualise sections within the project.
colourRed = '\033[0;31m'  # Red Seperator
revertColour = '\033[0;30m'  # We now revert the ANSI formatting otherwise it will stay as Red throughout.
dataSeperator = colourRed + "\n" * 3 + '*' * 113 + "\n"*3 + revertColour


# Import our gold historical data and look at the head
goldDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\gold_monthly_csv.csv')
print("Gold Dataframe :\n", goldDf.head(), dataSeperator)

# Import our Cryptocurrency historical coin data and look at the head
cryptoDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\coin_Bitcoin.csv')
print("Bitcoin Dataframe :\n", cryptoDf.head(), dataSeperator)


# Section 1 Data Cleanup of goldDf


# Inspect the dataframe
print(goldDf.info())
print(goldDf.shape)
print(goldDf.describe())
print(goldDf.columns,dataSeperator)

# Change the date to European Format
goldDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')

# Insert a new column that shows name of the asset we are using , in this case Gold
goldDf.insert(0, "Name", "Gold")
cryptoDf.insert(0, "Name", "Bitcoin")
# Summary statistics for goldDf
goldMinD = goldDf["Date"].min()
goldMaxD = goldDf["Date"].max()
print("Gold Minimum date: ", goldMinD)
print("Gold Maximum date: ", goldMaxD)
print("Gold Median Price: ", goldDf["Price"].median())
print("Gold Minimum Price: ", goldDf["Price"].min())
print("Gold Maximum Price: ", goldDf["Price"].max())
print("Gold Var: ", goldDf["Price"].var())
print("Gold Standard deviation: ", goldDf["Price"].std(), dataSeperator)


# Check for any Null Values in the Data
nullValues2 = 0
nullValues = goldDf.isna().sum().sum()
print("There are: ", nullValues, " Null values in the Dataset", dataSeperator)


# In commodity Trading we refer to the closing price as the settlement price for several reasons.
# I will rename the price column to this as it will be easier for colleagues to follow the data.
goldDf.rename(columns={'Price': 'Settlement'}, inplace=True)
print(goldDf.head(), dataSeperator)


# Section 2 Data Cleanup of cryptoDf

# Inspect the dataframe
print(cryptoDf.info())
print(cryptoDf.shape)
print(cryptoDf.describe())
print(cryptoDf.columns,dataSeperator)

nullValues2 = 0
nullValues = goldDf.isna().sum().sum()
print("There are: ", nullValues, " Null values in the Dataset", dataSeperator)


# Rename Closing price to Settlement
cryptoDf.rename(columns={'Close': 'Settlement'}, inplace=True)
print(cryptoDf.head(), dataSeperator)

# Change the datetime.datetime to a datetime.date object to remove the 23.59.59 and Set to European format.
cryptoDf["Date"] = pd.to_datetime(cryptoDf["Date"]).dt.strftime('%d-%m-%Y')
goldDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')
goldDf['Date'] = pd.to_datetime(goldDf.Date)
cryptoDf["Date"] = pd.to_datetime(cryptoDf.Date)
print(cryptoDf.head(), dataSeperator)

# Check that our dates are now in the right format
print("The Bitcoin Date Column is of Datatype: ", cryptoDf["Date"].dtype)
print("The Gold Date Column is of Datatype: ", goldDf["Date"].dtype, dataSeperator)

# We need to ascertain what our date ranges are for each dataset
goldMinD = goldDf["Date"].min()
goldMaxD = goldDf["Date"].max()
bitCoinMinD = cryptoDf["Date"].min()
bitCoinMaxD = cryptoDf["Date"].max()
print("Gold Minimum Date: ",goldMinD," Bitcoin Minimum Date: ",bitCoinMinD )
print("Gold Maximum Date: ",goldMaxD," Bitcoin Maximum Date: ",bitCoinMaxD, dataSeperator )


# Join our two dataframes with an inner join Date will be our PK
goldBitcoin = goldDf.merge(cryptoDf,on="Date")

# Remove columns that are not needed
goldBitcoin = goldBitcoin.drop(labels=["Open","High","Low","Adj Close","Volume"], axis=1,)
# Rename columns
goldBitcoin.rename(columns={"Name_x" : "Commodity","Settlement_x" : "Gold Settled Price", "Name_y":"Cryptocurrency","Settlement_y":"Bitcoin Settled Price" }, inplace=True)
# Rearrange the columns
goldBitcoin = goldBitcoin[["Date","Commodity","Gold Settled Price","Cryptocurrency","Bitcoin Settled Price"]]

print(goldBitcoin.head(10),dataSeperator)

#Look at our data using some basic plots







# Section  3:
# Create new Lists for analysis between Bitcoin and Gold with the columns we require.


#
#
# bitcoinList = []
# for index, rows in cryptoDf.iterrows():
#     newBitcoinList = [rows.Name, rows.Date, rows.Settlement]
#     bitcoinList.append(newBitcoinList)

# goldDf.sort_values("Date", ascending=True)
# print(goldDf)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
