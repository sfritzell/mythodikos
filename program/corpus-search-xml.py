#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

"""
Code for Mythodikos Project:
1. iterates through corpus
2. opens file, parses file, finds pattern matches with regex values & keys in a dictionary
3. locates secondary pattern matches with regex values within initial search results
4. for each match: records latinized person name (key), place name, geodata, title & author of text (needs some refinement), citation (with some issues), text context, context length and file name
5. writes geoJSON formatted information to .json file

Next Steps:
1. clean up citation extraction, author and title (prioritize other "Next Steps" first)
2. write to download/access most recent Perseus corpus and Pleiades file (nice to have, save for later with expanded dataset)

@author: sfritzell
adapted from: search-xml-greek.py
"""

# =====================================================================
# Imports & Modules
# =====================================================================

import os # to search file directory
import fnmatch # to specify files
import re # to use regex functions to search keywords
from bs4 import BeautifulSoup # to read xml files
import json # to write search results to json
from person_file import persondict # to read the person search terms from seperate file
from place_file import placedict # to read the place search terms from seperate file
from collections import	defaultdict # to create new entry based on unique id

# =====================================================================
# Functions
# =====================================================================

def get_context(line): #function to get the text context for search matches from xml
	context = '' #create empty variable for context
	rent = line.parent #the exact section of .xml text in which the match is found
	if rent.name == 'l': #if text uses lines/line numbers, get the immediate, previous, and following lines
		try:
			sib1 = rent.previous_sibling.previous_sibling.string #the line before the match line
			sib2 = rent.next_sibling.next_sibling.string #the line after the match line
			context_big = sib1 + ' ' + line + ' ' + sib2 #string of three lines
		except:
			try:
				context_big = sib1 + ' ' + line #if there's no line following the match line, return a string of two lines
			except:
				try:
					context_big = line + ' ' + sib2 #if there's no line before the match line, return a string of two lines
				except:		
					context_big = line #if there's no lines before or after match line, return the match line
	else: #if the text doesn't use lines/line numbers, get the text chunk of the match
		context_big = line.replace('\n', ' ') #replaces newline characters in the text chunk with space
	sentences = re.split("[.;·]", context_big) #split the context_big text chunks at major punctuation breaks
	for sentence in sentences: #for each string in the text chunk
		con_match = re.search(per, sentence) #if there is a keyword match in the string
		if con_match:
			context = sentence 
	return context #print the sting as match context

def make_citation(line, text): #function to get the full citaiton information for search matches using previously made functions
	cite_item = '' #create empty string to hold citation info

	text_title = soup.title.string #create variable for text title - needs some refining to grab just text title and not xml title, might be lower in file
	if soup.author: #if an author is recorded for the file
		text_author = soup.author.string #create a variable for text author
	else: 
		text_author = '' #otherwise record text author as blank

	def get_section(line): #function to get the section citation info from xml
		cite_list = [] #creates empty list for citation information
		for parent in line.parents: #for parents of keyword match
			if parent.name == 'div': #if the parent is a div
				if parent.attrs['type'] == 'textpart': #and if the div has textpart as an attibute
					try:
						cite_list.append(parent.attrs['subtype']+parent.attrs['n']) #grab the subtype (book, chapter, section) and the number
					except KeyError: #if this doesn't work for one instance, keep going
						continue
				else: continue #if the div doesn't have this attribute, keep going
			elif 'div' in parent.name: #if the the xml encoding is differnt, div might be in the parent name
				try:
					cite_list.append(parent.attrs['type']+parent.attrs['n']) #in that case, grab the type and number
				except KeyError:
					continue
		cite_list.reverse() #make the citation order: book,chapter,section
		citation = '.'.join(cite_list) #make format: book.chapter.section
		return citation #print the citation

	def get_linenum(line): #separated from get_section to test, function to get the line number citation info from xml
		textchunk = line.parent #the exact section of .xml text in which the match is found (could be a paragraph or a line)
		line_num = '' #create an empty variable for the line number
		for chunk in textchunk: #for each element in textchunk
			if textchunk.name == 'l' or 'lb': #if the textchunk is marked as a line
				try:
					line_num = textchunk.name + textchunk['n'] #line number is "line"+number
				except KeyError: #if this doesn't work for one instance, keep going
					continue
			else: #if textchunk isn't marked as a line, keep going
				continue
		return line_num #print the line number

	cite_item = text_author + ' , ' + text_title + ' , ' + get_section(line) + '.' + get_linenum(line) + ':' + text
	return cite_item

def make_jobj(dict1, dict2): #function to merge complex dicts at correct level and build geoJSON file
	geoj = {'type': 'FeatureCollection', 'features': []}
	for key in dict1:
		if key in dict2: #if the key in both dicts matches
			dict2[key]['properties']['citations'] = dict1[key] #add the value of said key from dict one at specified level in dict2
	for key in dict2:
		geoj['features'].append(dict2[key]) #append dict of values for each dict2 key to geoJSON features list
	return geoj

# =====================================================================
# Program
# =====================================================================

greekcorpusdir = "~/mythodikos/canonical-greekLit-master" #directory with files for text mining
outfile = "~/mythodikos/corpus-test-12-18.json" #file to write search data, change file type to .json with .json search

#build geojson file with desired search metadata
with open(outfile, 'w') as z: #to access/create the outfile for data from text-mining

	citations = defaultdict(list) #create default dict to collect citations for person-place pairs in list class
	pair_data = {} # new dict for other stuff on ids 

	for root, dirs, files in os.walk(greekcorpusdir): #iterate through files/directories in specified
		for file in files:
			if fnmatch.fnmatch(file, '*grc*.xml'): #for each file in the directory marked as Greek 
				infile = root+'/'+str(file) #identify these files to be searched
				
				with open(infile) as x: #open and iterate through each identifed file
					soup = BeautifulSoup(x, features='lxml')

					for person in persondict: #iterate through persondict; external file in same directory
						per_terms = persondict[person] #call value list /alt spellings for each person key
						for per in per_terms: #iterate through value list / alt spellings
							per_matches = soup.find_all(string=re.compile(per)) #find matches in text with alt spellings; using soup.find_all in place of re.search for navigating xml
							for per_match in per_matches: #iterate through matches
								context = get_context(per_match) #get text surrounding the match

								for place in placedict: #iterate through placedict; external file in same directory
									pl_keys = placedict[place] #define list of keys for each place item
									pl_terms = pl_keys['spellings'] #call values under specificed key
									pl_id = pl_keys['pleiades id']
									pl_gps = pl_keys['coordinates']
									for term in pl_terms: #iterate through alt spellings
										pair = re.search(term, context) #find matches in context with alt spellings; using re.search because context has been 'pulled' from xml
										if pair:
											citation = make_citation(per_match, context) #create citation for found matches
										else:
											continue

										ID = person +'-'+ place #create unique identifier for match pair
										citations[ID].append(citation) #in citedict creates key for ID (if new) and appends citation as value in list
										pair_data[ID] = {
											'type': 'Feature', 
											'geometry': {'type': 'Point', 'coordinates': pl_gps}, 
											'properties': {'title': place, 'pleiades id': pl_id, 'person connection': person, 'citations': []}
											} #in datadict creates key for ID and relevant values; does not need to append bc this data is /not/ citation dependent
	
	features = make_jobj(citations, pair_data) #combine dict data into geoJSON readable format
	json.dump(features, z, indent=4) #writes entries to json outfile (use json.dumps to continue work within program)

