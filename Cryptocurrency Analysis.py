# Certificate in Data Analytics for Finance
# Cian Murray cian.murray@capspire.com
# 15/04/2021
# Datasets Urls:
# https://finance.yahoo.com/quote/BTC-USD/history/
# https://finance.yahoo.com/quote/ETH-USD/history?period1=1514764800&period2=1546214400&interval=1mo&filter=history&
    # frequency=1mo&includeAdjustedClose=true
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
colourGreen = '\033[0;32m'
revertColour = '\033[0;30m'  # We now revert the ANSI formatting otherwise it will stay as Red throughout.
dataSeperator = colourRed + "\n" * 3 + '*' * 113 + "\n" * 3 + revertColour

# Import our gold historical data and look at the head
goldDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\gold_monthly_csv.csv')
print("Gold Dataframe :\n", goldDf.head(), dataSeperator)

# Import our Cryptocurrency historical coin data and look at the head
cryptoDf = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\coin_Bitcoin.csv')
print("Bitcoin Dataframe :\n", cryptoDf.head(), dataSeperator)

# The cryptoDf data frame has considerable more information than the goldDf, Cleanup and alignment  is required.


# Inspect the dataframe
print(goldDf.info(), dataSeperator)
print(goldDf.shape, dataSeperator)
print(goldDf.describe(), dataSeperator)
print(goldDf.columns, dataSeperator)

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

nullValues = goldDf.isna().sum().sum()
print("There are: ", nullValues, " Null values in the Gold Dataset", dataSeperator)
nullValues2 = cryptoDf.isna().sum().sum()
print("There are: ", nullValues2, " Null values in the crypto Dataset", dataSeperator)


# Create a Function to check dataframes easily for  null values

def null_loc(df): return df[df.isna().any(axis=1)]


# look at our null values
print(null_loc(cryptoDf), dataSeperator)
# As we only have one row to delete with no data we can simply drp it.
cryptoDf = cryptoDf.drop(labels=79, axis=0)
print(null_loc(cryptoDf), dataSeperator)


# In commodity Trading we refer to the closing price as the settlement price for several reasons.
# I will rename the price column to this as it will be easier for colleagues to follow the data.
goldDf.rename(columns={'Price': 'Settlement'}, inplace=True)
print(goldDf.head(), dataSeperator)

# Inspect the crypto dataframe
print(cryptoDf.info())
print(cryptoDf.shape)
print(cryptoDf.describe())
print(cryptoDf.columns, dataSeperator)


# Double check null values
nullValues2 = cryptoDf.isna().sum().sum()
print("There are: ", nullValues2, " Null values in the crypto Dataset", dataSeperator)

# Rename Closing price to Settlement
cryptoDf.rename(columns={'Close': 'Settlement'}, inplace=True)
print(cryptoDf.head(), dataSeperator)

# Change the datetime.datetime to a datetime.date object to remove the 23.59.59 and Set to European format.
cryptoDf["Date"] = pd.to_datetime(cryptoDf["Date"]).dt.strftime('%d-%m-%Y')
goldDf["Date"] = pd.to_datetime(goldDf["Date"]).dt.strftime('%d-%m-%Y')
goldDf['Date'] = pd.to_datetime(goldDf.Date)
cryptoDf["Date"] = pd.to_datetime(cryptoDf.Date)

# Check that our dates are now in the right format
print("The Bitcoin Date Column is of Datatype: ", cryptoDf["Date"].dtype)
print("The Gold Date Column is of Datatype: ", goldDf["Date"].dtype, dataSeperator)

# We need to ascertain what our date ranges are for each dataset and have a look at max prices
goldMinD = goldDf["Date"].min()
goldMaxD = goldDf["Date"].max()
bitCoinMinD = cryptoDf["Date"].min()
bitCoinMaxD = cryptoDf["Date"].max()
goldMaxPrice = goldDf["Settlement"].max()
bitcoinMaxPrice = cryptoDf["Settlement"].max()
print("Gold Minimum Date: ", goldMinD, " Bitcoin Minimum Date: ", bitCoinMinD, " Gold Max Price: ", goldMaxPrice)
print("Gold Maximum Date: ", goldMaxD, " Bitcoin Maximum Date: ", bitCoinMaxD, " Bitcoin Max Price", bitcoinMaxPrice,
      dataSeperator)

# # Create Scatter Plots to check for Data outliers
# cryptoDf.plot(x="Date",y="Settlement", kind="scatter",title="Bitcoin Outliers")
# plt.show()
# goldDf.plot(x="Date",y="Settlement", kind="scatter",title="Gold Outliers")
# plt.show()

# Join our two dataframes with an inner join Date will be our PK
# cryptoDf date time will now aggregate from days to month.
goldBitcoin = goldDf.merge(cryptoDf, on="Date")

# Remove columns that are not needed
goldBitcoin = goldBitcoin.drop(labels=["Open", "High", "Low", "Adj Close", "Volume"], axis=1, )
# Rename columns
goldBitcoin.rename(columns={"Name_x": "Commodity", "Settlement_x": "Gold Settled Price", "Name_y": "Cryptocurrency",
                            "Settlement_y": "Bitcoin Settled Price"}, inplace=True)
# Rearrange the columns
goldBitcoin = goldBitcoin[["Date", "Commodity", "Gold Settled Price", "Cryptocurrency", "Bitcoin Settled Price"]]

# Sort Df to make sure dates are consecutive with ascending = True
goldBitcoin = goldBitcoin.sort_values("Date", ascending=True)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(goldBitcoin, dataSeperator)

# Check for any null values in the Joined Dataset
nullValues3 = goldBitcoin.isna().sum().sum()
print("There are: ", nullValues3, " Null values in the Gold/Bitcoin Dataset", dataSeperator)

#  First I wish to look at price volatility over the last 2 years
# 2020-01-01 is the Max date range I wish to use as I am only interested in Pre covid volatility.
goldBitcoin["Date"] = pd.to_datetime(goldBitcoin["Date"])
rangeMask = (goldBitcoin["Date"] > "2018-01-01") & (goldBitcoin["Date"] <= "2020-01-01")
print(goldBitcoin.loc[rangeMask])

#  Secondly I wish to look at price volatility over the last 5 years
goldBitcoin["Date"] = pd.to_datetime(goldBitcoin["Date"])
rangeMask = (goldBitcoin["Date"] > "2016-01-01") & (goldBitcoin["Date"] <= "2020-01-01")
print(goldBitcoin.loc[rangeMask])

# Variables used for plotting
date = goldBitcoin["Date"]
gSp = goldBitcoin["Gold Settled Price"]
btcSp = goldBitcoin["Bitcoin Settled Price"]

# # Gold  Plot
# plt.plot(date, gSp, color="black", linestyle="--", label="Gold")
# plt.xlabel("Date")
# # Bitcoin  Plot
# plt.plot(date, btcSp, color="orange", linestyle="solid", label="Bitcoin")
# plt.ylabel("Settlement Price $")
# plt.title("Historical Bitcoin & Gold Prices", color="red")
# plt.legend()
# plt.show()

# Analysis 1

# Find the monthly Percentage change
goldBitcoin.insert(5, "GLD % Change", "")
goldBitcoin.insert(6, "BTC % Change", "")
print(goldBitcoin.head(), dataSeperator)

goldBitcoin["GLD % Change"] = \
    (goldBitcoin["Gold Settled Price"].diff()*100)/goldBitcoin["Gold Settled Price"].shift()
goldBitcoin["BTC % Change"] = \
    (goldBitcoin["Bitcoin Settled Price"].diff()*100)/goldBitcoin["Bitcoin Settled Price"]\
    .shift()


with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(goldBitcoin, dataSeperator)

# Replace NaN with 0 as it is the first value and will be zero
goldBitcoin["GLD % Change"] = goldBitcoin["GLD % Change"].fillna(0)
goldBitcoin["BTC % Change"] = goldBitcoin["BTC % Change"].fillna(0)


# Get the Maximum Volatility for Bitcoin
bitCoinVolatility = goldBitcoin["BTC % Change"].max()

# Get the Maximum volatility for Gold
goldVolatility = goldBitcoin["GLD % Change"].max()

# Average volatility for Bitcoin
bitCoinVolatilityMean = goldBitcoin["BTC % Change"].mean()

# Average volatility for Gold
goldVolatilityMean = goldBitcoin["GLD % Change"].mean()

# Volatility Summary Overall from Df
print("Bitcoin Max Volatility: ", bitCoinVolatility, "\nBitcoin Average Volatility : ", bitCoinVolatilityMean)
print("Gold Max Volatility: ", goldVolatility, "\nBitcoin Average Volatility: ", goldVolatilityMean, dataSeperator)

# 2018 volatility
data18 = [goldBitcoin["Date"],goldBitcoin["GLD % Change"],goldBitcoin["BTC % Change"]]
header = ["Date","Gold Volatility 2018","Bitcoin Volatility 2018"]
volatility2018 = pd.concat(data18,axis=1,keys=header)
volatility2018["Date"] = pd.to_datetime(goldBitcoin["Date"])
dateMask18 = (volatility2018["Date"] >= "2018-01-01") & (volatility2018["Date"] <= "2018-12-31")
volatility2018 = volatility2018.loc[dateMask18]
print(volatility2018, dataSeperator)

# 2019 volatility
data19 = [goldBitcoin["Date"],goldBitcoin["GLD % Change"],goldBitcoin["BTC % Change"]]
header = ["Date","Gold Volatility 2019","Bitcoin Volatility 2019"]
volatility2019 = pd.concat(data19,axis=1,keys=header)
volatility2019["Date"] = pd.to_datetime(goldBitcoin["Date"])
dateMask19 = (volatility2019["Date"] >= "2019-01-01") & (volatility2019["Date"] <= "2019-12-31")
volatility2019 = volatility2019.loc[dateMask19]
print(volatility2019, dataSeperator)

print(
    "                     2018 Volatility \n\n"
    "Max Gold Volatility 2018 :         ",volatility2018["Gold Volatility 2018"].max(),"\n"
    "Min Gold Volatility 2018 :         ",volatility2018["Gold Volatility 2018"].min(),"\n"                                                                                
    "Average Gold Volatility 2018:      ",volatility2018["Gold Volatility 2018"].mean(),"\n"
    "Max Bitcoin Volatility 2018:       ",volatility2018["Bitcoin Volatility 2018"].max(),"\n"
    "Min Bitcoin Volatility 2018 :      ",volatility2018["Bitcoin Volatility 2018"].min(),"\n"
    "Average Bitcoin Volatility 2018:   ",volatility2018["Bitcoin Volatility 2018"].mean(),"_"*30,"\n"
    "                     2019 Volatility \n\n"
    "Max Gold Volatility 2019 :       ",volatility2019["Gold Volatility 2019"].max(),"\n"
    "Min Gold Volatility 2019 :       ",volatility2019["Gold Volatility 2019"].min(),"\n"                                                                                
    "Average Gold Volatility 2019:    ",volatility2019["Gold Volatility 2019"].mean(),"\n"
    "Max Bitcoin Volatility 2019:     ",volatility2019["Bitcoin Volatility 2019"].max(), "\n"
    "Min Bitcoin Volatility 2019 :    ",volatility2019["Bitcoin Volatility 2019"].min(),"\n"      
    "Average Bitcoin Volatility 2019: ",volatility2019["Bitcoin Volatility 2019"].mean(), "_" * 30, "\n",dataSeperator
)
# Plotting or Volatility
date19 = volatility2019["Date"]
gldVol19 = volatility2019["Gold Volatility 2019"]
btcVol19 = volatility2019["Bitcoin Volatility 2019"]
date18 = volatility2018["Date"]
gldVol18 = volatility2018["Gold Volatility 2018"]
btcVol18 = volatility2018["Bitcoin Volatility 2018"]

# # 2018 plot
# plt.plot(date18, gldVol18, color="black", linestyle="--", label="Gold")
# plt.xlabel("Date")
# plt.plot(date18, btcVol18, color="orange", linestyle="solid", label="Bitcoin")
# plt.ylabel("Volatilty % of price")
# plt.title("Gold & Bitcoin Price Volatility 2018", color="red")
# plt.legend()
# plt.show()
# # 2019 Plot
# plt.plot(date19, gldVol19, color="black", linestyle="--", label="Gold")
# plt.xlabel("Date")
# plt.plot(date19, btcVol19, color="orange", linestyle="solid", label="Bitcoin")
# plt.ylabel("Volatility %  of price")
# plt.title("Gold & Bitcoin Price Volatility 2019", color="red")
# plt.legend()
# plt.show()


# Analysis 2:

# Is there any other cryptocurrency that we can use instead of Bitcoin , Lets look at etherium


# Taking the Monthly aggregated data from yahoo finance, we will create a dict to store our 2018 etherium data
etherData18 = \
    {
        "Date": ["2018-01-01", "2018-02-01", "2018-03-01", "2018-04-01", "2018-05-01", "2018-06-01", "2018-07-01",
                 "2018-08-01", "2018-09-01", "2018-10-01", "2018-11-01", "2018-12-01"],
        "Name": ["Etherium","Etherium","Etherium","Etherium","Etherium","Etherium","Etherium","Etherium",
                 "Etherium","Etherium","Etherium","Etherium"],
        "Etherium Settlement" : [775.76, 1119.37, 856.01, 397.25, 670.46, 578.67, 455.24, 433.87, 283.50, 233.22, 197.54, 113.40]
}
# Convert our Dict to a df
ether18 = pd.DataFrame(data=etherData18)
print(ether18, dataSeperator)

# Taking the Monthly aggregated data from yahoo finance, we will create a list to store our 2019 etherium data

etherData19 = [["2019-01-01",133.42,"Etherium"],["2019-02-01",107.15,"Etherium"],["2019-03-01",136.84,"Etherium"],
               ["2019-04-01",141.47,"Etherium"],["2019-05-01",162.19,"Etherium"],["2019-06-01",268.43,"Etherium"],
               ["2019-07-01",290.27,"Etherium"],["2019-08-01",218.55,"Etherium"],["2019-09-01",172.46,"Etherium"],
               ["2019-10-01",180.21,"Etherium"],["2019-11-01",183.80,"Etherium"],["2019-12-01",152.49,"Etherium"]]
columns = ["Date","Etherium Settlement","Name"]
ether19 = pd.DataFrame(data=etherData19, columns=columns)
# Rearrange the columns
ether19 = ether19[["Date", "Name", "Etherium Settlement"]]

print(ether19, dataSeperator)
print(null_loc(ether18), dataSeperator)
print(null_loc(ether19), dataSeperator)

# Get Etherium Volatility by year
ether18.insert(3, "ETH % Change", "")
ether18["ETH % Change"] = \
    (ether18["Etherium Settlement"].diff()*100)/ether18["Etherium Settlement"]\
    .shift()
ether18["ETH % Change"] = ether18["ETH % Change"].fillna(0)
print(ether18, dataSeperator)
ether19.insert(3, "ETH % Change", "")
ether19["ETH % Change"] = \
    (ether19["Etherium Settlement"].diff()*100)/ether19["Etherium Settlement"]\
    .shift()
ether19["ETH % Change"] = ether19["ETH % Change"].fillna(0)
print(ether19, dataSeperator)

# What Months have had negative change in 2019
for index, row in ether19.iterrows():
    if row["ETH % Change"] < 0:
        print("Date: ",row["Date"],"\n""Settlement: ",row["Etherium Settlement"], "   ",
                "\n% Change from Previous day: ",colourRed,row["ETH % Change"], revertColour,"\n","_" * 30, "\n")
    elif row["ETH % Change"] >= 0:
        print("Date: ", row["Date"], "\n""Settlement: ", row["Etherium Settlement"], "   ",
              "\n% Change from Previous day: ", colourGreen, row["ETH % Change"], revertColour, "\n", "_" * 30, "\n")
print(dataSeperator)

print(ether18.info(),"\n",ether19.info(),dataSeperator)
ether18["Date"] = pd.to_datetime(ether18["Date"])
ether19["Date"] = pd.to_datetime(ether19["Date"])

print(ether18.info(),"\n",ether19.info(),dataSeperator)


# Visualise our GoldBitcoin Data in a easy to follow format like Etherium
# I wish to look at these individually so i will separate the loop below
print("Gold Volatility Index \n\n","_" * 30, "\n")
for index, row in goldBitcoin.iterrows():
    if row["GLD % Change"] < 0:
        print("Date: \n ", row["Date"].strftime("%Y %b %d"),"\n""Gold % Change: ", "   ",
                "\n% Change from Previous day: ",colourRed,row["GLD % Change"], revertColour,"\n")
    elif row["GLD % Change"] >= 0:
        print("Date: \n", row["Date"].strftime("%Y %b %d"),"\n""Gold % Change: ", "   ",
              "\n% Change from Previous day: ", colourGreen, row["GLD % Change"], revertColour, "\n")
print(dataSeperator)
print("Bitcoin Volatility Index \n\n","_" * 30, "\n")
for index, row in goldBitcoin.iterrows():
    if row["BTC % Change"] < 0:
        print("Date: \n ", row["Date"].strftime("%Y %b %d"),"\n""BTC % Change: ", "   ",
                "\n% Change from Previous day: ",colourRed,row["BTC % Change"], revertColour,"\n")
    elif row["BTC % Change"] >= 0:
        print("Date: \n", row["Date"].strftime("%Y %b %d"),"\n""BTC % Change: ", "   ",
              "\n% Change from Previous day: ", colourGreen, row["BTC % Change"], revertColour, "\n")
print(dataSeperator)

# Join etherium dataframes
# join btc/gold volatility onto etherium volatility
# present a graph on volatility
# candlestick graphs on all 4 volatilities
# numpy
