

from xai.brain.wordbase.verbs._fuel import _FUEL

#calss header
class _FUELLED(_FUEL, ):
	def __init__(self,): 
		_FUEL.__init__(self)
		self.name = "FUELLED"
		self.specie = 'verbs'
		self.basic = "fuel"
		self.jsondata = {}
