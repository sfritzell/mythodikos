# anther file to brainstrom text-mining approaches through proximity search

# define "person" and "place" variables as lists, ultimately in Greek
person = [Arion, Atalanta]
	Arion = ['Arion', 'Arious', 'Ariou']
	Atalanta = ['Atalanta', 'Atalanti', 'Atalantae', 'Atalantan']

place = [Thebes, Athens, Corinth, Acadia]
	# Here the variables from list "place" must be defined in the same way as "person"


# to search for regular expressions in an XML file using "person" and "place" variables
import re
import xml.etree.ElementTree as ET 

# I need some way to tell my code to access the right XML files.  This may have something to do with path directory?

# I need a way of using re to search for use of "place" within 5 words (before and after) occurance of "person"
# This is one such framework adopted from a response to a similar question on stackoverflow. I don't entirely understand it.
match_to_5_words = '( [^ ]*){0,5} ?'
match_person = '(' + '|'.join(person) + ')'
match_place = '(' + '|'.join(place) + ')'
context_before = match_place + match_to_5_words + match_person
context_after = match_person + match_to_5_words + match_place
find_person_place = re.compile('(' + context_before + '|' + context_after + ')')

# This is part of the same stackoverflow framework, this time to extract metadata.  I don't fully understand it, and I'm not sure if it will work for my purposes.
copy_metadata = []
for filename in filenames:
	filestring = open(filename, 'rb').read()
	# tokenization could happen here for better word segmentation
	# use http://www.nltk.org/api/nltk.tokenize.html
	if re.search(find_person_place, filestring):
		print "Person-place connection found."
		# get the metadata
		metadata = pull_metadata(filename, filestring)
		copy_metadata.append(metadata)