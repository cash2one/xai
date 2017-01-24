#!/usr/bin/evn python
from xai.memory.memory import create_noun
import os

def read_cambtionary(data_file = 'cambtionary'):
	# filename = 'words/test.dat'
	# filename = '/usr/share/dict/linux.words'
	from pycambtionary import Pycambtionary
	import json

	mydict = Pycambtionary(data_file = data_file)
	mydict.read_database()

	for word, species in mydict.jsonword.items():
		# print(word, definitions)
		for specie, definitions in species.items():
			print(specie)
			if 'verb' in specie:
				pass
				if not os.path.exists('../memory/objects/_{}.py'.format(word)):
					create_noun(word, definitions)
			elif 'noun' in specie:
				if not os.path.exists('../memory/objects/_{}.py'.format(word)):
					create_noun(word, definitions)
			elif 'adj' in specie:
				pass
			elif 'adv' in specie:
				pass
			elif 'pre' in specie:
				pass
			elif 'suffix' in specie:
				pass
			elif 'pro' in specie:
				pass

def read_wikipedia():
	#
	pass