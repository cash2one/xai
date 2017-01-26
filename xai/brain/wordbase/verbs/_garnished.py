

from xai.brain.wordbase.verbs._garnish import _GARNISH

#calss header
class _GARNISHED(_GARNISH, ):
	def __init__(self,): 
		_GARNISH.__init__(self)
		self.name = "GARNISHED"
		self.specie = 'verbs'
		self.basic = "garnish"
		self.jsondata = {}
