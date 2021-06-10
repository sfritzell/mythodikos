#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
Code for Mythodikos projcect:
1. Iterate through corpus
2. Open text file, read file, check for matches
3. Turn raw text into nltk text object
4. Return 5 words before and after each keyword match 
5. Write results to csv

Next Steps:
* find word matches with (placenames)
* beautiful soup for xml searching
* use of regex (personnames) instead of lists
* turn chunks of code into functions
* return full sentence of keyword match instead of 5 words using TokenizeSentence (cltk) or similar

"""

import nltk # natural language toolkit - http://www.nltk.org/
from nltk import word_tokenize
# import re
# import pprint ?
import greek_accentuation # library for accenting and analyzing accentuation of Ancient Greek words
from greek_accentuation.characters import base
# from greek_accentuation.characters import strip_accent
from greek_accentuation.characters import strip_breathing
import os
import csv

# =====================================================================
# Functions
# =====================================================================

# Determines whether a text contains any keywords and returns a list of matching keywords

def word_matches(wordlist, text_obj):
	matches = []
	for word in wordlist:
		if word in text_obj:
			matches.append(word)
		else:
			continue
	return matches

# =====================================================================
# Program
# =====================================================================

outfile = "/Users/stellafritzell/mythodikos/test-1-23.csv"

f = csv.writer(open(outfile, 'w'))
f.writerow(['filename', 'keyword', 'index', 'context'])

keywords = []

greekcorpusdir = "/Users/stellafritzell/mythodikos/cannonical-greekLit-master"

# iterates through files and subfolders in directory containing the corpus
for root, dirs, files in os.walk(greekcorpusdir):
	for filename in files:
		infile = root + '/' + filename
		with open(infile) as fp:
			raw = fp.read() # stores contents of file
			matches = word_matches(keywords, raw) # searches file contents for keyword matches
			if len(matches) == 0: # if no matches exist, move on to next file
				continue
			else: # if matches exist
				tokens = word_tokenize(raw) # tokenizes raw text
				text = nltk.Text(tokens) # creates a Text object for nltk functions
				for counter, value, in enumerate(text): # identifies index numbers for each word
					for key in matches: # iterates through present matching keywords
						if value == key: # for each match, creates 10-word slice around keyword
							first = counter - 6
							last = counter + 6
							result = text[first:last]
							# writes the filename, relevant keyword, index number, and context
							f.writerow([filename, key, counter, result])
						else:
							continue