#!/usr/bin/python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import string

inputfile   = sys.argv[1]
excludefile = sys.argv[2]

file = open(inputfile, "r")
ex_file = open(excludefile, "r").read().split()

# Using counter to create a dict subclass with words & # of occurrence
wordcount = Counter(file.read().split())

# Convert dict wordcount to lowercase
wordcount = {k.lower(): v for k, v in wordcount.items()}

# Creating Dataframe from above dict with index orientation
dataFrame = pd.DataFrame.from_dict(wordcount, orient='index').reset_index()

# renaming columns in dataframe
dataFrame = dataFrame.rename(columns={'index': 'word', 0: 'count'})

# exclude the data in dataframe from exclude list
dataFrame = dataFrame[~dataFrame.word.isin(ex_file)]

# Adding column percent & calculating percentage
dataFrame['percent'] = dataFrame['count']/(dataFrame['count'].sum())*100

# sort dataframe by percent
dataFrame = dataFrame.sort_values(by = 'percent', ascending = False)

# Plotting in Graph
top10 = dataFrame['word'][:10]
axis = np.arange(len(top10))
freq = dataFrame['count'][:10]
plt.bar(axis, freq, align='center')
plt.xticks(axis, top10, rotation = 50, fontsize = 10)
plt.xlabel('Word')
plt.ylabel('Count')
plt.title('Top 10 Words and Occurences')
plt.show()
