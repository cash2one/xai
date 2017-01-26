

from xai.brain.wordbase.adjectives._feminine import _FEMININE

#calss header
class _FEMININES(_FEMININE, ):
	def __init__(self,): 
		_FEMININE.__init__(self)
		self.name = "FEMININES"
		self.specie = 'adjectives'
		self.basic = "feminine"
		self.jsondata = {}
