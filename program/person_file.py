#!/usr/bin/venv python 3
# -*- coding: utf-8 -*-

'''
Python dictionary object for Mythodikos project; Latinized person names and varient original language spellings

* compiled in reference to https://www.theoi.com/greek-mythology/heroes.html ; eventually LIMC

@author: sfritzell
'''

persondict = {
'Achilles': [r'\bἈχιλλε', r'\bἈχιλλέ', r'\bἈχιλε', r'\bἈχιλέ'], #may be getting some false results, double check regex
'Actaeon': [r'\bἈκταίων', r'\bἈκταίον'],
'Adonis': [r'Ἄδωνις', r'Ἄδωνιν', r'\bἈδώνιδ', r'\bἈδωνίδ'], #overlap with festival / month names
'Amymone': [r'\bἈμυμώνη', r'\bἈμυμώνῃ', r'\bἈμυμώνα', r'\bἈμυμῶνα', r'\bἈμυμόνη'], #also the name of a river
'Andromeda': [r'\bἈνδρομέδα', r'\bἈνδρομέδᾳ', r'\bἈνδρομέδη', r'\bἈνδρομέδῃ'],
'Antiope': [r'\bἈντιόπ'],
'Arachne': [r'\bἈράχνη', r'\bἈράχνῃ'],
'Arion': [r'\bἈρίων', r'\bἈρίον'], #also the name of a horse
'Ascalabus': [r'\bἈσκάλαβο'],
'Asclepius': [r'\bἈσκληπιό', r'\bἈσκληπιο', r'\bἈσκλήπιο', r'Ἀσκληπιέ', r'\bἈσκλαπ'],
'Atalanta': [r'\bἈταλάντ'],
'Bellerophon': [r'\bΒελλερεφόντα', r'\bΒελλεροφόντα', r'\bΒελερόφοντα', r'\bΒελλερεφόντη', '\bΒελλερεφόντῃ', r'\bΒελλεροφόντῃ', r'\bΒελλεροφόντη', r'\bΒελεροφόντη', r'\bΒελλεροφόντο', r'\bΒελλερόφοντο', r'\bΒελερόφοντο', r'\bΒελεροφόντο', r'\bΒελλεροφώ', r'\bΒελλεροφῶ'],
'Busiris': [r'\bΒούσιρι', r'\bΒουσίριδ'],
'Cadmus': [r'Κάδμε', r'\bΚάδμοι', r'\bΚάδμον', r'\bΚάδμος', r'\bΚάδμου', r'\bΚάδμω', r'\bΚάδμῳ'],
'Callisto': [r'\bΚαλλιστώ', r'Καλλιστῆς', r'Καλλιστοῖ', r'Καλλιστοῦς'],
'Cecrops': [r'\bΚέκροψ', r'\bΚέκρωψ', r'\bΚέκροπο', r'\bΚέκροπα', r'\bΚέκροπε', r'\bΚεκρόπε', r'Κέκροπι'],
'Coronis': [r'Κορωνίς', r'\bΚορωνίδα', r'\bΚορωνίδο', r'\bΚορωνίδι'], #there are multiple Coronises
'Cycnus': [r'\bΚύκνο', r'\bΚύκνῳ', r'\bΚύκνω', r'Κύκνε'], #there are multiple Cycnuses, typically identified by toponym --> seperation will occur in search/data collection
'Cyparissus': [r'\bΚυπάρισσο', r'\bΚυπαρίσσο', r'\bΚυπαρισσο', r'\bΚυπάριτ', r'\bΚυπαρίτ'], #also a city name
'Cyrene': [r'\bΚυρήνη', r'\bΚυρήνῃ', r'\bΚυράνα', r'\bΚυράνᾳ'], #also a city name
'Danae': [r'\Δανάη', r'\bΔανάῃ', r'\bΔανάα'],
'Deucalion': [r'\bΔευκαλίω', r'\bΔευκαλλίω'],
'Diomedes': [r'\bΔιομήδη', r'\bΔιομήδῃ', r'\bΔιομήδο', r'\bΔιομήδε', r'\bΔιόμηδε'], #may be getting some false results, overlap with female name Diomede, adjectival use
'Endymion': [r'\bἘνδυμίων'],
'Erysichthon': [r'\bἘρυσίχθ', r'\bἘρισίχθ'],
'Eryx': [r'Ἔρυξ', r'Ἔρυκα', r'\bἘρύκη', r'\bἘρύκῃ', r'\bἜρυκι', r'\bἜρυκο'], #there are multiple Eryxes, also a city name, TLG finds only a feminine name - contrast with male figure in THEOI
'Europa': [r'\bΕὐρώπη', r'\bΕὐρώπῃ', r'\bΕὐρώπα', r'\bΕὐρώπᾳ'], #also a place name, may be getting some false results
'Euadne': [r'\bΕὐάδν'], #there are multiple Euadnes
#'Ganymede': [r'\b'],
#'Geryon': [r'\b'],
#'Heracles': [r'\b'],
'Hippolyta': [r'\bἹππολύτα', r'\bἹππολύτη'],
#'Hyacinthus': [r'\b'],
#'Iamus': [r'\b'],
#'Iasion': [r'\b'],
#'Icarius': [r'\b'],
#'Io': [r'\b'],
#'Ixion': [r'\b'],
#'Jason': [r'\b'],
#'Leda': [r'\b'],
#'Lycaon': [r'\b'],
#'Lycurgus': [r'\b'],
'Meleager': [r'\bΜελέαγρ', r'\bΜελεάγρ'], #may be getting some false results, overlap with festival name
'Midas': [r'\bΜίδα', r'\bΜίδᾳ', r'\bΜίδη', r'Μίδου', r'Μίδῃ', r'Μίδεω', r'\bΜῖδα'],
#'Minyades': [r'\b'], #a trio of princesses
'Narcissus': [r'\bΝάρκισσο', r'\bΝαρκίσσο', r'Ναρκίσσῳ', r'\bΝάρκισο', r'\bΝαρκίσο'],
#'Odysseus': [r'\b'],
#'Oedipus': [r'\b'],
#'Orestes': [r'\b'],
#'Orion': [r'\b'],
#'Otrera': [r'\b'],
#'Pandora': [r'\b'],
'Pasiphae': [r'\bΠασιφάη', r'\bΠασιφάῃ', r'\bΠασιφάα'],
'Pelops': [r'\bΠέλο'], #accent should limit results in regex
#'Penthesilea': [r'\b'],
#'Perseus': [r'\b'],
#'Phaethon': [r'\b'],
#'Psyche': [r'\b'],
#'Pygmalion': [r'\b'],
#'Pyrrha': [r'\b'],
#'Salmoneus': [r'\b'],
#'Sisyphus': [r'\b'],
#'Tantalus': [r'\b'],
#'Tennes': [r'\b'],
#'Theseus': [r'\b'],
#'Tithonus': [r'\b'],
#'Triptolemus': [r'\b'],
#'Tyro': [r'\b']
} 

