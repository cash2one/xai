

from xai.brain.wordbase.nouns._cardinal import _CARDINAL

#calss header
class _CARDINALS(_CARDINAL, ):
	def __init__(self,): 
		_CARDINAL.__init__(self)
		self.name = "CARDINALS"
		self.specie = 'nouns'
		self.basic = "cardinal"
		self.jsondata = {}
