

from xai.brain.wordbase.adjectives._possessive import _POSSESSIVE

#calss header
class _POSSESSIVES(_POSSESSIVE, ):
	def __init__(self,): 
		_POSSESSIVE.__init__(self)
		self.name = "POSSESSIVES"
		self.specie = 'adjectives'
		self.basic = "possessive"
		self.jsondata = {}
