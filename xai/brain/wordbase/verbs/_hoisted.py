

from xai.brain.wordbase.verbs._hoist import _HOIST

#calss header
class _HOISTED(_HOIST, ):
	def __init__(self,): 
		_HOIST.__init__(self)
		self.name = "HOISTED"
		self.specie = 'verbs'
		self.basic = "hoist"
		self.jsondata = {}
