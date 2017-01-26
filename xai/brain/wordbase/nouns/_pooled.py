

from xai.brain.wordbase.nouns._pool import _POOL

#calss header
class _POOLED(_POOL, ):
	def __init__(self,): 
		_POOL.__init__(self)
		self.name = "POOLED"
		self.specie = 'nouns'
		self.basic = "pool"
		self.jsondata = {}
