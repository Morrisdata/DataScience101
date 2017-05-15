# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:24:29 2017

@author: Matthew
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
movies = pd.read_csv('~\Desktop\Python_for_Data-master\Data\movies.csv')
ratings = pd.read_csv('~\Desktop\Python_for_Data-master\Data\\ratings.csv')
links = pd.read_csv('~\Desktop\Python_for_Data-master\Data\\links.csv')
tags = pd.read_csv('~\Desktop\Python_for_Data-master\Data\\tags.csv')

# EXPLORATORY ANALYSIS

# Movies
movies.dtypes # data types of each column
movies # print the first 30 and last 30 rows
type(movies) # DataFrame
movies.head() # print the first 5 rows
movies.head(10) # print the first 10 rows
movies.tail() # print the last 5 rows
movies.index # "the index" (aka "the labels")
movies.columns # column names (which is "an index")
movies.shape # number of rows and columns
movies.values # underlying numpy array

# summarize (describe) the DataFrame
movies.describe() # describe all numeric columns
movies.describe(include=['object']) # describe all object columns
movies.describe(include='all') # describe all columns

# summarize a Series
movies.genres.describe() # describe a single column



# ## Bar Plot: show a numerical comparison across different categories			
			
# count the number of countries in each continent			
movies = movies.genres.value_counts()
movies
movies=movies.head(100)




			
# compare with bar plot			
movies.genres.value_counts().plot(kind='bar')			

movies

# ratings
ratings.dtypes # data types of each column
ratings # print the first 30 and last 30 rows
type(ratings) # DataFrame
ratings.head() # print the first 5 rows
ratings.head(10) # print the first 10 rows
ratings.tail() # print the last 5 rows
ratings.index # "the index" (aka "the labels")
ratings.columns # column names (which is "an index")
ratings.shape # number of rows and columns
ratings.values # underlying numpy array

# summarize (describe) the DataFrame
ratings.describe() # describe all numeric columns
ratings.describe(include=['object']) # describe all object columns
ratings.describe(include='all') # describe all columns

# summarize a Series
ratings.genres.describe() # describe a single column



# links
links.dtypes # data types of each column
links # print the first 30 and last 30 rows
type(links) # DataFrame
links.head() # print the first 5 rows
links.head(10) # print the first 10 rows
links.tail() # print the last 5 rows
links.index # "the index" (aka "the labels")
links.columns # column names (which is "an index")
links.shape # number of rows and columns
links.values # underlying numpy array

# summarize (describe) the DataFrame
links.describe() # describe all numeric columns
links.describe(include=['object']) # describe all object columns
links.describe(include='all') # describe all columns

# summarize a Series
links.genres.describe() # describe a single column




# tags
tags.dtypes # data types of each column
tags # print the first 30 and last 30 rows
type(tags) # DataFrame
tags.head() # print the first 5 rows
tags.head(10) # print the first 10 rows
tags.tail() # print the last 5 rows
tags.index # "the index" (aka "the labels")
tags.columns # column names (which is "an index")
tags.shape # number of rows and columns
tags.values # underlying numpy array

# summarize (describe) the DataFrame
tags.describe() # describe all numeric columns
tags.describe(include=['object']) # describe all object columns
tags.describe(include='all') # describe all columns

# summarize a Series
tags.genres.describe() # describe a single column








# VISUAL EXPLORATION OF DATA

# compare with histogram
movies.counts.plot(kind='hist', bins=6)
whsgrp.RINGTIME.plot(kind='hist', bins=6)
whsgrp.TOTAL_CUSTOMER.plot(kind='hist', bins=6)
whsgrp.ITEMSOLD.plot(kind='hist', bins=6)
