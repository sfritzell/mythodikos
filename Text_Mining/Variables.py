# This file is to define the "person" and "place" variables for the Mythodikos Project (Text Mining)

# for all definition lists, will it be possible to define items without accents?  This would simplify entries.
# "lemma", the dicitionary entry will be most useful.  It might exclude some alternate spellings, but will allow for easy conjugation to define variables

person = [Arion, Atalanta]
	
	Arion = ['Ἀρίων','Ἀρίονος','Ἀρίονα','Ἀρίον','Ἀρίονι','Ἀρίωνα','Ἀρίωνι','Ἀρίωνος',
			'Arion','Ariona','Arionem','Arioniam','Arionis','Arioniae','Arionium','Arione']

	Atalanta = ['Ἀταλάντη','Ἀταλάντης','Ἀταλάντα','Ἀταλάνται','Ἀταλάνταις','Ἀταλάντας','Ἀταλάντῃ','Ἀταλάντην',
			'Atalanta','Atalantae','Atalantam','Atalantaeos','Atalantaeas','Atalantes','Atalante','Atalanten']

	# Latin will also add -que to nouns, which Greek does not do.  How to account for this?  RE?
	# similarly Latin use of "V" for "U" in some texts - Perseus may be catching this as they digitize
	# names shared between person variables may need to be defined by another key word (i.e. Arion, and Arion_hippos)

place = [place_A]

	# two-word place names, temples not included, since I am interested in more general places.
	# seperate varables for each letter will make any edits to the code easier to complete.

place_A = [Abai, Abdera, Abia, Abrettene, Abydos, Acarnania, Acharnai, Achelous, Acheron, Acroceraunia, Actium, 
		Adrasteia, Aegae, Aegaeon, Aegiale, Aegilia, Aegina, Aeolis, Agrinion, Aiane, Aidepsos, Aigeira, Aigeiros, 
		Aigosthena, Ainos, Aiolidai, Aisepos, Aixone, Akidon, Akragas, Akrai, Akraiphiai, 
		Akroterion, Akrothooi, Alalkomenai, Albanopolis, Alea, Alexandreia, Alkomenai, Almopia, Alope, Alopeke, 
		Aloros, Alpenos, Alyattes, Alyzia, Amnisos, Amorgos, Ampelos, Amphanai, Amphikleia, Amphipolis, Amphissa, 
		Amphitrope, Amyklai, Anactorium, Anaia, Anakaia, Anaphe, Anaphlystos, Anapos, Anastasioupolis, Andania, 
		Andros, Ankyra, Antandros, Anthedon, Anthemous, Antigoneia, Antikyra, Antissa, Aperlae, Aphidna, 
		Aphrodisias, Aphrodisios, Aphroditia, Apidanos, Apollonia, Apollonis, Aptera, Arabia, Araphen, Aratthos, 
		Arethousa, Argeia, Argilos, Argolis, Argos, Ariste, Arkadia, Arkonnesos, Arne, Aroania, Artemision, 
		Arycandus, Asia, Asine, Askania, Asopos, Aspis, Assos, Astakos, Asterion, Astraia, Astypalaia, Astyra, 
		Atalante, Atarneus, Atene, Athamania, Athenaion, Athene, Athos, Athyras, Atrax, Attaleia, Attea, Attica, 
		Aulai, Aulis, Aulon, Axios, Azanes, Azania, Azoros]

	# places that a direct name with a person variable will cause difficulty, i.e. Atalanta & Achelous - define in reference to further geographical term (island)
	# place names are occasionally shared by multiple georaphic places (see Ainos/Aenus) - a reference term may be needed in these cases as well

	Abai = ['Ἄβαι','Ἀβαί','Ἀβαὶ','Ἄβαις','Ἀβαῖς','Ἀβαῖσι','Ἀβάν','Ἄβαντα','Ἀβάντων','Ἄβας','Ἄβῃσι','Ἄβα','Ἄβη']

	Abdera = ['Ἄβδηρα','Ἄβδαρα','Ἀβδείροις','Ἄβδηρ','Ἀβδηρά','Ἀβδηρὰ','Ἄβδηραν','Ἀβδήροις','Ἀβδήροισι','Ἀβδήροισιν','Ἄβδηρον','Ἄβδηρος','Ἄβδηρου','Ἀβδήρῳ','Ἀβδήρωι','Ἀβδήρων','Ἀβδηρῶν','Αὐδήρων',
			'Abdera','Abderam','Abderae','Abdere']

	Abia = ['Ἀβία','Ἀβιά','Ἀβιὰ','Ἀβιᾶ','Ἀβιᾶν','Ἀβιάς','Ἀβιού','Ἀβιοὺ','Ἀβιοῦ']

	Abrettene = ['Ἀβρεττηνή','Ἀβρεττηνὴ','Ἀβρετάνη','Ἀβρετίνη','Ἀβρεττηνῆς','Ἀβρεττηνοὶ','Ἀβρεττηνοί','Ἀβρεττηνός','Ἀβρεττηνοῦ',
			'Abretteni']

	Abydos = ['Ἄβυδος','Ἄβιδος','Ἀβύδῃ','Ἄβυδοι','Ἄβυδον','Ἀβύδου','Ἀβύδῳ','Ἀβύδων',
			'Abydos','Abydo','Abydon','Abydi','Abydum','Abydus']

	Acarnania = ['Ἀκαρνανία','Ἀκαρνανίᾳ','Ἀκαρνανίαι','Ἀκαρνανίαν','Ἀκαρνανίας','Ἀκαρνανίης','Ἀκαρνία',
			'Ἀκαρνάν','Ἀκαρναῖος','Ἀκαρνᾶνα','Ἀκαρνανάδες','Ἀκαρνᾶνας','Ἀκαρνᾶνε','Ἀκαρνᾶνι','Ἀκαρνᾶνος','Ἀκαρνάνων','Ἀκαρνανῶν','Ἀκαρνᾶσι','Ἀκαρνᾶσιν','Ἀκαρνῆνα','Ἀκαρνιαίου','Ἀκαρνιαίων','Ἀκαρνούς','Ἀκάρνων','Ἀκαρνπῶν',
			'Acarnania','Acarnanam','Acarnan','Acarnanes','Acarnanas','Acarnaniae','Acarnaniam','Acarnanum','Acarnanicae','Acarnane','Acarnana']

	Acharnai = ['Ἀχάρναι','Ἀχαρναί','Ἀχαρναὶ','Ἀχάρναις','Ἀχαρναῖς','Ἀχάρνας','Ἀχαρνάς','Ἀχάρνη','Ἀχαρνὴ','Ἀχαρνή','Ἀχάρνης','Ἀχαρνῶν',
			'Acharnae','Acharneus','Acharne']

	Achelous = ['᾽χελῶε','᾽χελῷε','Ἀχελήϊον','᾽Ἀχελήϊος','Ἀχελοῖος','Ἀχελῷ','Ἀχελῷε','Ἀχελώϊον','Ἀχελώιον','Ἀχελῶιον','Ἀχελώϊος','Ἀχελώιος','Ἀχελῶιος','Ἀχελώιου','Ἀχελωίου','Ἀχελωΐου','Ἀχελωίῳ','Ἀχελώιωι','Άχελῷν','Ἀχελώνιος',
			'Ἀχελωνίῳ','Ἀχελῷοι','Ἀχελῶον','Ἀχελῷον','Ἀχελῴος','Ἀχελῶος','Ἀχελῷος','Ἀχελωός','Ἁχελῷος','Ἀχελώου','Ἀχελῴου','Ἀχελώῳ','Ἀχελῴω','Ἀχελῴῳ',
			'Achelous','Acheloum','Acheloi','Acheloia','Achelois','Acheloo','Acheloium','Acheloidas','Acheloon','Acheloe','Acheloius']

		# Name Achelous also name of river god

	Acheron = ['Ἀχέρονθ᾽','Ἀχέροντ','Ἀχἐροντ᾽','Ἀχέροντα','Ἀχέροντας','Ἀχέροντες','Ἀχέροντι','Ἀχέροντος','Ἀχέρων',
			'Axheron','Acherontem','Acheronte','Acherontis','Acheronta']

	Acroceraunia = ['Ἀκροκεραυνία','Ἀκροκεραυνίας','Ἀκροκεραυνίοις','Ἀκροκεραυνίων',
			'Acroceraunia','Acroceraunio','Acroceraunium','Acrocerauniis']

	Actium = ['Ἀκτία','Ἀκτίᾳ','Ἀκτίαν','Ἄκτιον','Ἀκτίου','Ἀκτίῳ','Ἀκτίωι',
			'Actium']

	Adrasteia = ['Ἀδράστεια','Ἀδραστείᾳ','Ἀδραστείαι','Ἀδραστεῖαι','Ἀδράστειαν','Ἀδραστείας','Ἀδρήστεια','Ἀδρηστείᾳ','Ἀδρήστειαν','Ἀδρηστείας','Ἀδρηστείης','Ἀδρηστία']

		# Name 'Adrasteia' also name of the nymph nurse of Zeus

	Aegae = ['Ἀγἀης','Αἰγαί','Αἰγαὶ','Αἰγαῖαι','Αἰγαίαις','Αἰγαίας','Αἰγαιέων','Αἰγαῖς','Αἴγας','Αἰγάς','Αἰγέαις','Αἰγέας','Αἶγες','Αἰγεῶν','Αἰγή','Αἰγὴ','Αἰγῶν',
			'Aegae','Aegaeo','Aegaei','Aegaea','Aegaeas','Aegaeum','Aegaeos','Aegaeis','Aegaeae']

	Aegaeon	= ['Αἰγαίοιο','Αἰγαίοις','Αἰγαίοισιν','Αἴγαιον','Αἰγαῖον','Αἰγαίου','Αἰγαίῳ','Αἰγαίωι','Αἰγαίων',
			'Aegaeon','Aegaeona','Aegaeonem','Aegaeonis','Aegaeoni']

		# Aegaeon might be combined with Aegea depending on how general these place definitions need to be

	Aegiale = ['Αἰγιάλη','Αἰγιάλην','Αἰγιάλης',
			'Aegialeus','Aegialeo','Aegiale','Aegiales','Aegialeon']

	Aegilia = ['Αἰγιλία','Αἰγιλιά','Αἰγιλιὰ','Αἰγιλίαν','Αἰγιλίας',
			'Aegilia','Aegilion']

	Aegina = ['Αἴγειναν','Αἰγείνης','Αἴγενα','Αἴγιν᾽','Αἴγινα','Αἰγίνᾳ','Αἴγιναν','Αἰγίνῃ','Αἰγίνηι','Αἰγίνης','Αἰγίννι',
			'Aegina','Aeginam','Aeginae','Aeginan','Aeginium','Aeginetis']

	Aeolis = ['Αἰοληΐδι','Αἰοληίδι','Αἰολί','Αἰολὶ','Αἰολίδ᾽','Αἰολίδα','Αἰολίδας','Αἰολίδες','Αἰολίδεσσι','Αἰολίδι','Αἰόλιδος','Αἰολίδος','Αἰολίδων','Αἴολις','Αἰολίς','Αἰολίσι','Αἰολίσιν','Αἰολίσσιν',
			'Aeolis','Aeoliam','Aeoliae','Aeolide','Aeolio','Aeolios','Aeoliis','Aeoliden','Aeolides','Aeolium','Aeoli','Aeoliorum','Aeolii','Aeolidis','Aeolida','Aeolidae','Aeolidos','Aeolia','Aeolicam','Aeolias','Aeolica','Aeolicae']

	Agrinion = ['Ἀγρίνιον']

	Aiane = ['Αἰανή','Αἰανὴ','Αἰανῆς']

	Aidepsos = ['Αἴδηψον','Αἰδηψόν','Αἴδηψος','Αἰδψός','Αἰδηψοῦ','Αἰδηψῷ','Αἰδηψῶι','Αἰδήψιον','Αἰδήψιος','Αἰδήψια',
			'Aedepso','Aedepsos']

	Aigeira = ['Αἴγειρα','Αἰγείρα','Αἰγείρᾳ','Αἴγειραν','Αἰγείρας']

	Aigeiros = ['Αἴγειρον','Αἰγείροιο','Αἴγειρος','Αἰγείρου','Αἰγείρω','Αἰγείρῳ']

	Aigosthena = ['Αἰγόσθενα','Αἰγοσθένεια','Αἰγοσθένειαν','Αἰγοσθενία','Αἰγοσθένοις','Αἰγοσθενεῖ','Αἰγοσθενεύς','Αἰγοσθενίτην',
			'Aegosthenenses']

	Ainos = ['Αἶνο','Αἶνον','Αἶνος','Αἴνου','Αἴνῳ','Αἴνωι',
			'Aenos','Aënos','Aenus']

		# Ainos could refer either to a mountain on Cephallonia, or to a town in Thrace (Aenus)
		# as a non-proper noun, Ainos means 'tale, story, song' - a reference term may be needed

	Aiolidai =

	Aisepos =

	Aixone =

	Akidon = 

	Akragas =

	Akrai =

	Akraiphiai =

	Akroterion =

	Akrothooi =

	Alalkomenai = 

	Albanopolis =

	Alea =

	Alexandreia =

	Alkomenai =

	Almopia =

	Alope =

	Alopeke =

	Aloros =

	Alpenos =

	Alyattes =

	Alyzia =

	Amnisos =

	Amorgos =

	Ampelos =

	Amphanai =

	Amphikleia =

	Amphipolis =

	Amphissa =

	Amphitrope =

	Amyklai =

	Anactorium =

	Anaia =

	Anakaia =

	Anaphe =

	Anaphlystos =

	Anapos =

	Anastasioupolis =

	Andania =

	Andros =

	Ankyra =

	Antandros =

	Anthedon =

	Anthemous =

	Antigoneia =

	Antikyra =

	Antissa =

	Aperlae =

	Aphidna =

	Aphrodisias =

	Aphrodisios =

	Aphroditia =

	Apidanos =

	Apollonia =

	Apollonis =

	Aptera =

	Arabia = ['Arabia','Arabiam','Arabiae']

	Araphen =

	Aratthos =

	Arethousa =

	Argeia =

	Argilos =

	Argolis =

	Argos =

	Ariste =

	Arkadia =

	Arkonnesos =

	Arne =

	Aroania =

	Artemision =

	Arycandus =

	Asia =

	Asine =

	Askania =

	Asopos =

	Aspis =

	Assos =

	Astakos =

	Asterion =

	Astraia =

	Astypalaia =

	Astyra =

	Atalante =

	Atarneus =

	Atene =

	Athamania =

	Athenaion =

	Athene =

	Athos =

	Athyras =

	Atrax =

	Attaleia =

	Attea =

	Attica =

	Aulai =

	Aulis =

	Aulon =

	Axios =

	Azanes =

	Azania =

	Azoros =