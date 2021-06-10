""" This program will allow a user to search a large TEI, XML, or CLTK text corpus 
for all connections between a variable "person" and all variables "place" within a 
certain proximity.  Each "person-place" connection will be saved to an Excel sheet 
along with {citation} and {excerpt} metadata """

# This program is built off of pseudocode for the Mythodikos project

import re

""" Here we define the person-list, with each list time refering to a regular
expression string that accounts for possible conjugations.  It will look something
like this: """
person = [Arion, Atalanta]
	Arion = re.compile(r^Ari.*, re.I)
	Atalante = re.compile(r'Atalant\D') # As a potential alternative to the method for Arion

""" The place-list will need to be formulated like the person list.  It will probably 
be more complicated since it will need to immediately contain more items in order to 
test the program """

place = 

# TODO: search text corpus for variable person
# to search using regex findall

Arion.findall(# import text corpus)
		# once proof of concept is developed, this could this work as person.findall ?

# to search using if-then statements
if person == Arion :
	# then: search TBD number of characters before and after person for variable "place"
	# if: single item from variable "place" occurs in specificed proximity to "person(Arion)"
		# then: record person-place connection and metadata (citation, excerpt) to excel spreadsheet
	# elif: multiple item from variable "place" occurs in specified proximity to "person(Arion)"
		# then: record instance of person(Arion) and metadata (citation, excerpt) in seperate excel spreadsheet
			# this functions to flag possible "catalogue" occurances for personal review
			# following review, reviewer can manually enter instance into primary spread sheet if a single connection can be found
	# else: do not record instance of "person(Arion)"

elif person == Atalante : 
# it might be possible to use elif statements for each {person}, copying the code from case to case, making exceptions or exclusions that are necessary

else :
	print('No results.')