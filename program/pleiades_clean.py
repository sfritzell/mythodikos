#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

'''
Code to clean Pleiades data file for use in the Mythodikos project
1. Opens Pleiades json file
2. Iterates through file data
3. Records desired data for each entry with of a particular place type

Next Steps:
1. Cross reference results with Greek corpus search terms
2. Expand place types, possibly to include: 'river', 'plain', 'pass', 'resevoir', 'cave', 'cape', 'hill', 'forest', 'mountain', 'island', 'water-open', 'province', 'lake', ...

@author: sfritzell
''' 

# =====================================================================
# Imports & Modules
# =====================================================================
import json

# =====================================================================
# Functions
# =====================================================================
def select_type(types): #to look at Pleiades items only of the specified types
	place_types = ['settlement', 'region', 'island']
	relevant = False
	for item in place_types:
		if item in types:
			relevant = True
			break
		else:
			continue
	return relevant

def get_names(name_info): #to get a list of alternate names for desired items
	romanized = []
	for n in name_info:
		item = n['romanized']
		romanized.append(item)
	return romanized


# =====================================================================
# Program
# =====================================================================

infile = "~/mythodikos/pleiades-places-latest.json"
# web url: http://atlantides.org/downloads/pleiades/json/pleiades-places-latest.json.gz

outfile = "~/mythodikos/clean-pleiades.json"

with open(outfile, 'w') as z:
	with open(infile) as x:
		data = json.load(x) #parses json file to python dictionary
		entries = []

		# print(data) #prints entire json file
		# for d in data:
			# print(d) #print top level keys

		for d in data["@graph"]:
			typ = d['placeTypes'] #type of place represented by entry
			name = d['title'] #common use (?) name of place
			pl_id = d['id'] #pleiades id number
			gps = d['reprPoint'] #representative lat-long coordinates
			alt_names = d['names'] #returns EVERYTHING under 'names', mostly non-essential

			if select_type(typ) == True:
				name_list = get_names(alt_names)
				entry = {'title': name, 'location type': typ, 'Pleiades id': pl_id, 'coordinates': gps, 'other names': name_list}

				entries.append(entry)

		json.dump(entries, z, indent=4) #print results in redable format to json outfile


