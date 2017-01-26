

from xai.brain.wordbase.verbs._fuel import _FUEL

#calss header
class _FUELLING(_FUEL, ):
	def __init__(self,): 
		_FUEL.__init__(self)
		self.name = "FUELLING"
		self.specie = 'verbs'
		self.basic = "fuel"
		self.jsondata = {}
