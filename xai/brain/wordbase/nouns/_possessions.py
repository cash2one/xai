

from xai.brain.wordbase.nouns._possession import _POSSESSION

#calss header
class _POSSESSIONS(_POSSESSION, ):
	def __init__(self,): 
		_POSSESSION.__init__(self)
		self.name = "POSSESSIONS"
		self.specie = 'nouns'
		self.basic = "possession"
		self.jsondata = {}
