

from xai.brain.wordbase.nouns._cache import _CACHE

#calss header
class _CACHED(_CACHE, ):
	def __init__(self,): 
		_CACHE.__init__(self)
		self.name = "CACHED"
		self.specie = 'nouns'
		self.basic = "cache"
		self.jsondata = {}
