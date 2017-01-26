

from xai.brain.wordbase.verbs._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKING(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKING"
		self.specie = 'verbs'
		self.basic = "overstock"
		self.jsondata = {}
