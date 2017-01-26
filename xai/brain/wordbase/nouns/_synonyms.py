

from xai.brain.wordbase.nouns._synonym import _SYNONYM

#calss header
class _SYNONYMS(_SYNONYM, ):
	def __init__(self,): 
		_SYNONYM.__init__(self)
		self.name = "SYNONYMS"
		self.specie = 'nouns'
		self.basic = "synonym"
		self.jsondata = {}
