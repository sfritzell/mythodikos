#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

"""
Code to read/write .json data for Mythodikos project

Place coordinates should come from pleiades-places-latest.json.gz

@author: sfritzell
"""

# =====================================================================
# Imports & Modules
# =====================================================================

import re
import json 

# =====================================================================
# Program
# =====================================================================

# a Python object (dict):
persondict = {
	'Atalanta': [r'\bἈταλάντ'], 
	'Arion': [r'\bἈρίων', r'\bἈρίον']
}

# convert into JSON, indented for easer reading
y = json.dumps(persondict, indent=4, sort_keys=True)

# the result is a JSON string --> the regex is in unicode
print(y)