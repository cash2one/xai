

from xai.brain.wordbase.nouns._rental import _RENTAL

#calss header
class _RENTALS(_RENTAL, ):
	def __init__(self,): 
		_RENTAL.__init__(self)
		self.name = "RENTALS"
		self.specie = 'nouns'
		self.basic = "rental"
		self.jsondata = {}
