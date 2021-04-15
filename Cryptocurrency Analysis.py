# Certificate in Data Analytics for Finance
# Cian Murray cian.murray@capspire.com
# 15/04/2021

# Datasets Urls:
# https://data.world/pmohun/complete-historical-cryptocurrency-financial-data
# https://datahub.io/core/gold-prices

# camelCase will be used as a coding standard throughout.

# numpy will be used for creating arrays and Algebra
# pandas to be used for importing of data and data manipulation.
import numpy as np
import pandas as pd
desired_width=400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)

# matplotlib and seaborn to be used for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns
colour = sns.color_palette()

# I created a data seperator in order to make it easier to visualise sections within the project.
colourRed = '\033[0;31m'  # Red Seperator
revertColour = '\033[0;30m'  # We now revert the ANSI formatting otherwise it will stay as Red throughout.
dataSeperator = colourRed + "\n" * 3 + '*' * 113 + "\n"*3 + revertColour

# Import our gold historical data and look at the head
goldDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\gold_monthly_csv.csv')
print (goldDf.head,dataSeperator)

# Import our Cryptocurrency historical coin data and look at the head
cryptoDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\consolidated_coin_data.csv')
print (cryptoDf.head,dataSeperator)


# Section 1 Data Cleanup of goldDf


# Inspect the dataframe
print(goldDf.info())
print(goldDf.shape)
print(goldDf.describe())
print(goldDf.columns,dataSeperator)


# Summary statistics for goldDf
print("Gold Minimum date: ",goldDf["Date"].min())
print("Gold Maximum date: ",goldDf["Date"].max())
print("Gold Median Price: ",goldDf["Price"].median())
print("Gold Minimum Price: ",goldDf["Price"].min())
print("Gold Maximum Price: ",goldDf["Price"].max())
print("Gold Var: ",goldDf["Price"].var())
print("Gold Standard deviation: ",goldDf["Price"].std(),dataSeperator)


#Check for any Null Values in the Data
nullValues2 = 0
nullValues = goldDf.isna().sum().sum()
print("There are: ",nullValues," Null values in the Dataset",dataSeperator)


# Add in a column to define what the Price/Dates are referencing, In this case it is Gold
goldDf.insert(1,"Commodity","Gold")
print(goldDf.head(),dataSeperator)


# Format the date to a more readable structure
goldDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')
print(goldDf.head(),dataSeperator)


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


