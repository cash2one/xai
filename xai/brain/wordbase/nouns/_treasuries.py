

from xai.brain.wordbase.nouns._treasury import _TREASURY

#calss header
class _TREASURIES(_TREASURY, ):
	def __init__(self,): 
		_TREASURY.__init__(self)
		self.name = "TREASURIES"
		self.specie = 'nouns'
		self.basic = "treasury"
		self.jsondata = {}
