# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:46:45 2020

@author: karun
"""
import pandas
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
data = pandas.read_csv(r"E:\McGill\MMA-2020\Text Analysis\Assignments\final_assignment1.csv")
##Randomly selecting 2500 rows

final = data.sample(n=2500)
Z = final.FullDescription

##Just to see what are the tokens
Tokens = Z.apply(word_tokenize)

# Tokenize into words
final['FullDescription'] = final['FullDescription'].map(lambda x: word_tokenize(x))


# Turn lists back to string
final['FullDescription'] = final['FullDescription'].map(lambda x: ' '.join(x))

alpha = pandas.Series(' '.join(final.FullDescription).split()).value_counts()[:5]
print(alpha)   ##Top 5 words with frequencies without removing the stop words


##Removing the Stop words
final1 = data.sample(n=2500)

# Tokenize into words
final1['FullDescription'] = final1['FullDescription'].map(lambda x: word_tokenize(x))

# filter out stop words
stop_words = set(stopwords.words('english'))
final1['FullDescription'] = final1['FullDescription'].map(lambda x: [w for w in x if not w in stop_words])


# Turn lists back to string
final1['FullDescription'] = final1['FullDescription'].map(lambda x: ' '.join(x))

beta = pandas.Series(' '.join(final1.FullDescription).split()).value_counts()[:5]
print(beta)   ##Top 5 words with frequencies without removing the stop words








