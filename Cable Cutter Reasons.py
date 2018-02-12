"""

1-31-2018

This code answers the question 'How many people who cut cable list both price
and use of streaming services as reasons?'. The source data is from a consumer
survey, and the results will be included in the 2017 fourth quarter report.

@author: eadlaf

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

# load the excel file with the data
data = pd.read_excel('F:\Tivo\Data Science Projects/2017Q4/analysis/eaQ5-data-Cable Cutter Reasons.xlsx')

# create a dataframe with only the columns of interest included
included_columns = ['Respondent', 'Reason_price', 'Reason_stream']
df = data[included_columns]

# define a function to index the dataframe by customer choice
def choice (dframe, column):
    notnull = dframe[column].notnull()
    choice_df = dframe[notnull]
    return choice_df

# count the number of rows in the indexed dataframe
def value (dframe):
    n = len(dframe)
    return n

# find the number of cord cutters who chose price
price = choice(dframe=df, column='Reason_price')
pricevalue = value(dframe=price)
pricevalue

# find the number of cord cutters who chose streaming
stream = choice(dframe=df, column='Reason_stream')
streamvalue = value(dframe=stream)
streamvalue

# find the number of cord cutters who chose both
priceandstream = choice(dframe=price, column='Reason_stream')
priceandstreamvalue = value(dframe=priceandstream)
priceandstreamvalue

# create a venn diagram of the values
venn2(subsets = (pricevalue, streamvalue, priceandstreamvalue), set_labels = ('Price Too High', 'Use Streaming Services'))
plt.show()
