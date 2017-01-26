

from xai.brain.wordbase.adjectives._obscene import _OBSCENE

#calss header
class _OBSCENER(_OBSCENE, ):
	def __init__(self,): 
		_OBSCENE.__init__(self)
		self.name = "OBSCENER"
		self.specie = 'adjectives'
		self.basic = "obscene"
		self.jsondata = {}
