#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

'''
Python dictionary object for Mythodikos project; Latinized place names and varient original language spellings

* compiled in reference to filtered Pleiades data, TLG lemma search for varient Greek spellings

* make into a dictionary of dictionaries to allow for pleiades info (# and coordinates) to be included and then easily appended to search results
e.g. {'Arcadia': {'spellings': [], 'pleiades id': , 'coordinates': []}}

@author: sfritzell
'''

placedict = {
	'Arcadia': 
	{
		'spellings': [r'\bἈρκαδ', r'\bἈρκάδ'],
		'pleiades id': '570102',
		'coordinates': [22.170246015828386, 37.61817012463577]
	},
	'Boeotia': 
	{
		'spellings': [r'\bΒοιωτ', r'\bΒοιῳτ', r'\bΒοϊωτ', r'\bΒοέκ', r'\bΒοεκ'],
		'pleiades id': '540689',
		'coordinates': [23.188078743333328, 38.34519476333334]
	},
	'Calydon': 
	{
		'spellings': [r'\bΚαλυδόν', r'\bΚαλύδων', r'\bΚαλυδῶν', r'\bΚαλυδών'],
		'pleiades id': '540699',
		'coordinates': [21.533182500000002, 38.372926]
	},
	'Colchis': 
	{
		'spellings': [r'\bΚόλκ', r'\bΚολκ', r'\bΚολχ'],
		'pleiades id': '874432',
		'coordinates': [39.228819, 38.52585]
	},
	'Corinth': 
	{
		'spellings': [r'\bΚόρινθ', r'\bΚορίνθ', r'\bΚορινθ'],
		'pleiades id': '570182',
		'coordinates': [22.88154529176389, 37.90639977908864]
	},
	'Lacedaemon': 
	{
		'spellings': [r'\bΛακεδ', r'\bΛαβεδ', r'\bΛακκοδ', r'\bΛακηδ', r'\bΛακιδ', r'\bΛακοδ', r'\bΛαχεδ'],
		'pleiades id': '570406',
		'coordinates': [22.460186899999997, 37.075742175]
	},
	'Lesbos': 
	{
		'spellings': [r'\bΛέσβε', r'\bΛέσβη', r'\bΛέσβο', r'\bΛέσβῳ', r'\bΛέσβω'],
		'pleiades id': '550696',
		'coordinates': [26.250159394099608, 39.16901707159906]
	},
	#'Lycaeus': [r''],
	#'Mainalos': [r''],
	#'Methymna': [r''],
	#'Parthenion': [r''],
	#'Taenarum': [r''],
	#'Tarentum': [r''],
	#'Tegea': [r''],
	'Thebes': 
	{
		'spellings': [r'\bΘήβ', r'\bΘῆβ'],
		'pleiades id': '541138',
		'coordinates': [23.317577, 38.319156]
	}
}


