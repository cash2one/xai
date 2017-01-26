

from xai.brain.wordbase.verbs._transliterate import _TRANSLITERATE

#calss header
class _TRANSLITERATES(_TRANSLITERATE, ):
	def __init__(self,): 
		_TRANSLITERATE.__init__(self)
		self.name = "TRANSLITERATES"
		self.specie = 'verbs'
		self.basic = "transliterate"
		self.jsondata = {}
