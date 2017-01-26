

from xai.brain.wordbase.nouns._garnish import _GARNISH

#calss header
class _GARNISHED(_GARNISH, ):
	def __init__(self,): 
		_GARNISH.__init__(self)
		self.name = "GARNISHED"
		self.specie = 'nouns'
		self.basic = "garnish"
		self.jsondata = {}
