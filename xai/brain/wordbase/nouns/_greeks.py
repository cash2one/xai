

from xai.brain.wordbase.nouns._greek import _GREEK

#calss header
class _GREEKS(_GREEK, ):
	def __init__(self,): 
		_GREEK.__init__(self)
		self.name = "GREEKS"
		self.specie = 'nouns'
		self.basic = "greek"
		self.jsondata = {}
