

from xai.brain.wordbase.nouns._porter import _PORTER

#calss header
class _PORTERS(_PORTER, ):
	def __init__(self,): 
		_PORTER.__init__(self)
		self.name = "PORTERS"
		self.specie = 'nouns'
		self.basic = "porter"
		self.jsondata = {}
