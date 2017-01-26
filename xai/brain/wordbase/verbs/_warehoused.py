

from xai.brain.wordbase.verbs._warehouse import _WAREHOUSE

#calss header
class _WAREHOUSED(_WAREHOUSE, ):
	def __init__(self,): 
		_WAREHOUSE.__init__(self)
		self.name = "WAREHOUSED"
		self.specie = 'verbs'
		self.basic = "warehouse"
		self.jsondata = {}
