

from xai.brain.wordbase.verbs._pool import _POOL

#calss header
class _POOLED(_POOL, ):
	def __init__(self,): 
		_POOL.__init__(self)
		self.name = "POOLED"
		self.specie = 'verbs'
		self.basic = "pool"
		self.jsondata = {}
