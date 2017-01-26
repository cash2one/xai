

from xai.brain.wordbase.verbs._drink import _DRINK

#calss header
class _DRINKS(_DRINK, ):
	def __init__(self,): 
		_DRINK.__init__(self)
		self.name = "DRINKS"
		self.specie = 'verbs'
		self.basic = "drink"
		self.jsondata = {}
