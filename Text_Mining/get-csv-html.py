#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

"""
Code to get and read pleiades-places-latest.csv file for Mythodikos project

@author: sfritzell
"""

# =====================================================================
# Imports & Modules
# =====================================================================

import requests #to open pleiades html file
import gzip #to unzip the file  #problems installing gzip with pip in terminal - how to fix?  this module is necessary for opening the .gz zip extension
import csv 

# =====================================================================
# Program
# =====================================================================

pleiades_data = "/Users/stellafritzell/mythodikos/pleiades-data.csv"  #where to save .csv data
pleiades_csv_url = "http://atlantides.org/downloads/pleiades/dumps/pleiades-places-latest.csv.gz" #url for zipped .csv file
download = requests.get(pleiades_csv_url) #access the zipped .csv file
# download.encoding = 'utf-8'


# with open(pleiades_data, 'w') as y: