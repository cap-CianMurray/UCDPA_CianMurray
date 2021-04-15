# Certificate in Data Analytics for Finance
# Cian Murray cian.murray@capspire.com
# 15/04/2021

# Datasets Urls:
# https://data.world/pmohun/complete-historical-cryptocurrency-financial-data
# https://datahub.io/core/gold-prices

# camelCase will be used as a coding standard throughout.

# numpy will be used for creating arrays and Algebra
import numpy as np
# pandas to be used for importing of data and data manipulation.
import pandas as pd
# matplotlib and seaborn to be used for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns
colour = sns.color_palette()

# I created a data seperator in order to make it easier to visualise sections within the project.
colourRed = '\033[0;31m'  # Red Seperator
revertColour = '\033[0;30m'  # We now revert the ANSI formatting otherwise it will stay as Red throughout.
dataSeperator = colourRed + "\n" * 3 + '*' * 113 + "\n"*3 + revertColour


# Import our Cryptocurrency historical coin data and look at the head and tail
cryptoDF = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\consolidated_coin_data.csv')
print (cryptoDF.head)
print (dataSeperator)
print (cryptoDF.tail)
print (dataSeperator)
# Import our gold historical data and look at the head and tail
goldDF = pd.read_csv(r'C:\Users\CianMurray\Documents\UCDPA_CianMurray_Datasets\gold_monthly_csv.csv')
print (goldDF.head)
print (dataSeperator)
print (goldDF.tail)
print (dataSeperator)