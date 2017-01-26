

from xai.brain.wordbase.adjectives._favorite import _FAVORITE

#calss header
class _FAVORITES(_FAVORITE, ):
	def __init__(self,): 
		_FAVORITE.__init__(self)
		self.name = "FAVORITES"
		self.specie = 'adjectives'
		self.basic = "favorite"
		self.jsondata = {}
