

from xai.brain.wordbase.verbs._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKS(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKS"
		self.specie = 'verbs'
		self.basic = "overstock"
		self.jsondata = {}
