

from xai.brain.wordbase.adjectives._favourite import _FAVOURITE

#calss header
class _FAVOURITES(_FAVOURITE, ):
	def __init__(self,): 
		_FAVOURITE.__init__(self)
		self.name = "FAVOURITES"
		self.specie = 'adjectives'
		self.basic = "favourite"
		self.jsondata = {}
