

from xai.brain.wordbase.nouns._dictionary import _DICTIONARY

#calss header
class _DICTIONARIES(_DICTIONARY, ):
	def __init__(self,): 
		_DICTIONARY.__init__(self)
		self.name = "DICTIONARIES"
		self.specie = 'nouns'
		self.basic = "dictionary"
		self.jsondata = {}
