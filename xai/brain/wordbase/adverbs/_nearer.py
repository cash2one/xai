

from xai.brain.wordbase.adverbs._near import _NEAR

#calss header
class _NEARER(_NEAR, ):
	def __init__(self,): 
		_NEAR.__init__(self)
		self.name = "NEARER"
		self.specie = 'adverbs'
		self.basic = "near"
		self.jsondata = {}
