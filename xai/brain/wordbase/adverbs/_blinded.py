

from xai.brain.wordbase.adverbs._blind import _BLIND

#calss header
class _BLINDED(_BLIND, ):
	def __init__(self,): 
		_BLIND.__init__(self)
		self.name = "BLINDED"
		self.specie = 'adverbs'
		self.basic = "blind"
		self.jsondata = {}
