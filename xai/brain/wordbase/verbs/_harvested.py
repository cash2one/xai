

from xai.brain.wordbase.verbs._harvest import _HARVEST

#calss header
class _HARVESTED(_HARVEST, ):
	def __init__(self,): 
		_HARVEST.__init__(self)
		self.name = "HARVESTED"
		self.specie = 'verbs'
		self.basic = "harvest"
		self.jsondata = {}
