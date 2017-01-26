

from xai.brain.wordbase.adjectives._unfair import _UNFAIR

#calss header
class _UNFAIRER(_UNFAIR, ):
	def __init__(self,): 
		_UNFAIR.__init__(self)
		self.name = "UNFAIRER"
		self.specie = 'adjectives'
		self.basic = "unfair"
		self.jsondata = {}
