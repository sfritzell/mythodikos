#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

'''
Python dictionary object for Mythodikos project; Latinized place names and varient original language spellings

* compiled in reference to filtered Pleiades data, TLG lemma search for varient Greek spellings

Next Steps:
1. Add group / ethinic names where appropriate; i.e. Argives under Argos

@author: sfritzell
'''

placedict = {
	#'Abae':
	#'Abantis': #Ancient name for Euboea
	#'Abdera':
	#'Abia':
	#'Abydon': #Also Amydon
	#'Acacesium':
	#'Academia':
	#'Acarnania':
	#'Acesa': #Also Lemnos
	#'Achaia': #Two, 1.) Aegialus province in the Peloponnese, 2.) south of Thessaly
	#'Achaarnae':
	#'Achelous': #rivers?
	'Argolis': 
	{
		'spellings': [r'\bἈργολί', r'\bἈργόλι', r'\bἈργολι'],
		'pleiades id': '570104',
		'coordinates': [22.962079770375375, 37.62145180121853]
	},
	'Argos':
	{
		'spellings': [r'\bἌργος', r'\bἌργου', r'\bἌργει'],
		'pleiades id': '491527',
		'coordinates': [22.719464, 37.631561]
	},
	'Arcadia': 
	{
		'spellings': [r'\bἈρκαδ', r'\bἈρκάδ'],
		'pleiades id': '570102',
		'coordinates': [22.170246015828386, 37.61817012463577]
	},
	#'Athens': ,
	#'Attica': ,
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
	'Mainalos': 
	{
		'spellings': [r'\bΜαίναλο', r'\bΜαινάλο', r'\bΜαινάλῳ', r'\bΜαινάλι', r'\bΜαιναλί'],
		'pleiades id': '570451',
		'coordinates': [22.265891, 37.549491]
	},
	'Megalopolis': 
	{
		'spellings': [r'\bΜεγαλόπολ', r'\bΜεγαλοπόλ', r'\bΜεγαλῃπόλ', r'\bμεγαλόπολ', r'\bμεγαλοπόλ', r'\bμεγαλῃπόλ', r'\bΜεγαλοπολ', r'\bμεγαλοπολ'],
		'pleiades id': '570467',
		'coordinates': [22.1273485, 37.412417500000004]
	},
	'Methymna':
	{
		'spellings': [r'\bΜήθυ', r'\bΜηθύ', r'\bΜεθυμ', r'\bΜίθυ', r'\bΜιθύ'],
		'pleiades id': '550738',
		'coordinates': [26.176890999999998, 39.369167000000004]
	},
	#'Parthenion': [r''], #two possible locations in Pleiades
	'Tainaron': 
	{
		'spellings': [r'\bΤαίναρο', r'\bΤαινάρο', r'\bΤαινάρῳ', r'\bΤαινάρω', r'\bΤαινάρι', r'\bΤαιναρί'],
		'pleiades id': '570702',
		'coordinates': [22.48650368203568, 36.401358569665966]
	},
	'Tarentum': 
	{
		'spellings': [r'\bΤάρας', r'\bΤάραντα', r'\bΤάραντι', r'\bΤάραντο', r'\bΤαράντ', r'\bΤέρεντο', r'\bΤερέντο', r'\bΤερεντό'],
		'pleiades id': '442810',
		'coordinates': [17.2330416, 40.4737866]
	},
	'Tegea': 
	{
		'spellings': [r'\bΤεγέα', r'\bΤέγεα', r'\bΤεγέᾳ', r'\bΤεγέη', r'\bΤεγέῃ'],
		'pleiades id': '570707',
		'coordinates': [22.420672, 37.455301]
	},
	'Thebes': 
	{
		'spellings': [r'\bΘήβ', r'\bΘῆβ'],
		'pleiades id': '541138',
		'coordinates': [23.317577, 38.319156]
	},
	'Trapezus':
	{
		'spellings': [r'\bΤραπεζόντ', r'\bΤραπεζούντ', r'\bΤραπεζοῦντ', r'\bΤραπεζούς', r'\bΤραπεζοῦς', r'\bΤραπεζῶντ'],
		'pleiades id': '570746',
		'coordinates': [22.060685, 37.456281]
	}
}


