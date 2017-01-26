

from xai.brain.wordbase.verbs._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKED(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKED"
		self.specie = 'verbs'
		self.basic = "overstock"
		self.jsondata = {}
