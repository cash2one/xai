

from xai.brain.wordbase.nouns._food import _FOOD

#calss header
class _FOODS(_FOOD, ):
	def __init__(self,): 
		_FOOD.__init__(self)
		self.name = "FOODS"
		self.specie = 'nouns'
		self.basic = "food"
		self.jsondata = {}
