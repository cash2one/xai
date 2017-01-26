

from xai.brain.wordbase.nouns._warehouse import _WAREHOUSE

#calss header
class _WAREHOUSED(_WAREHOUSE, ):
	def __init__(self,): 
		_WAREHOUSE.__init__(self)
		self.name = "WAREHOUSED"
		self.specie = 'nouns'
		self.basic = "warehouse"
		self.jsondata = {}
