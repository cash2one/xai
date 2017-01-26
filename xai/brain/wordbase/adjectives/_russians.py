

from xai.brain.wordbase.adjectives._russian import _RUSSIAN

#calss header
class _RUSSIANS(_RUSSIAN, ):
	def __init__(self,): 
		_RUSSIAN.__init__(self)
		self.name = "RUSSIANS"
		self.specie = 'adjectives'
		self.basic = "russian"
		self.jsondata = {}
