

from xai.brain.wordbase.nouns._reputation import _REPUTATION

#calss header
class _REPUTATIONS(_REPUTATION, ):
	def __init__(self,): 
		_REPUTATION.__init__(self)
		self.name = "REPUTATIONS"
		self.specie = 'nouns'
		self.basic = "reputation"
		self.jsondata = {}
