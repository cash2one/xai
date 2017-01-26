

from xai.brain.wordbase.adverbs._slow import _SLOW

#calss header
class _SLOWER(_SLOW, ):
	def __init__(self,): 
		_SLOW.__init__(self)
		self.name = "SLOWER"
		self.specie = 'adverbs'
		self.basic = "slow"
		self.jsondata = {}
