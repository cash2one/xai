

from xai.brain.wordbase.nouns._rating import _RATING

#calss header
class _RATINGS(_RATING, ):
	def __init__(self,): 
		_RATING.__init__(self)
		self.name = "RATINGS"
		self.specie = 'nouns'
		self.basic = "rating"
		self.jsondata = {}
