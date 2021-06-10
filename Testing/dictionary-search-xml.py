#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

"""
Code for Mythodikos Project:
1. opens file, parses file, finds pattern matches with keys from a dictionary ({name varient: latinzied name})
2. for each key match: records latinized name, title & author of text, citation, and text context (text line, one line before and after)
3. writes information to .csv

Next Steps:
1. search multiple fies
2. compile place-name search terms using place_names.csv (has nominative greek & latinized forms, & Pleiades id) and lemmatized search and/or regex (for adjectives)
3. find word matches with placenames


@author: sfritzell
adapted from: search-xml-greek.py
"""

# =====================================================================
# Imports & Modules
# =====================================================================

import re # to use regex functions
from bs4 import BeautifulSoup # to read xml files
import csv

# =====================================================================
# Functions
# =====================================================================

def get_citation(line):
	sections = [parent.attrs for parent in m.parents if parent.name == 'div'] # a list with each 'div' element and attributes as a dictionary
	cite_list = []
	for s in sections: # for each 'div' attributes dictionary
		if s['type'] == 'textpart': # for any 'div' demarkating a section of text
			cite_list.append(s['n']) # return the number of that text part
		else: 
			continue
	cite_list.reverse()
	citation = '.'.join(cite_list)
	return citation

# =====================================================================
# Program
# =====================================================================

infile = "/Users/stellafritzell/mythodikos/canonical-greekLit-master/data/tlg0001/tlg001/tlg0001.tlg001.perseus-grc2.xml"
outfile = "/Users/stellafritzell/mythodikos/corpus-test-2-14.csv"

persondict = {
	'Ἀταλάντη': 'Atalanta', 'Ἀταλάντης': 'Atalanta', 'Ἀταλάντα': 'Atalanta', 'Ἀταλάνται': 'Atalanta', 'Ἀταλάνταις': 'Atalanta', 'Ἀταλάντας': 'Atalanta', 'Ἀταλάντῃ': 'Atalanta', 'Ἀταλάντην': 'Atalanta',
	'Ἀρίων': 'Arion', 'Ἀρίωνι': 'Arion', 'Ἀρίωνα': 'Arion', 'Ἀρίωνος': 'Arion', 'Ἀρίον': 'Arion', 'Ἀρίονος': 'Arion', 'Ἀρίονα': 'Arion', 'Ἀρίονι': 'Arion'
	}

with open(infile) as f:
	soup = BeautifulSoup(f, features='lxml')
	# cleansoup = strip_length(strip_accents(strip_breathing(soup.find_all('l')))) # removes accents and breath marks from text elements only


# build .csv with desired metadata as column headers
with open(outfile, 'w') as z:
	f = csv.writer(z)
	f.writerow(['person', 'title', 'author', 'citation', 'context'
		#, 'filename'
		])
	
	text_title = soup.title.string
	text_author = soup.author.string

	for key in persondict:
		name = persondict[key]
		matches = soup.find_all(string=re.compile(key))

		for m in matches: # m = occurance of matching string
			linematch = m.parent # linematch represents the line containing m
			linenumber = m.parent['n'] # line number attribute of line match
			prev_line = linematch.previous_sibling.previous_sibling.string
			next_line = linematch.next_sibling.next_sibling.string
			context = [prev_line, m, next_line]
			citation = get_citation(linematch) + '.' + linenumber # this appends line number to the section numbers in standard format

			f.writerow([name, text_title, text_author, citation, context])

