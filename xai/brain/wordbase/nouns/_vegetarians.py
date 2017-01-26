

from xai.brain.wordbase.nouns._vegetarian import _VEGETARIAN

#calss header
class _VEGETARIANS(_VEGETARIAN, ):
	def __init__(self,): 
		_VEGETARIAN.__init__(self)
		self.name = "VEGETARIANS"
		self.specie = 'nouns'
		self.basic = "vegetarian"
		self.jsondata = {}
