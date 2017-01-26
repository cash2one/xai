

from xai.brain.wordbase.nouns._registry import _REGISTRY

#calss header
class _REGISTRIES(_REGISTRY, ):
	def __init__(self,): 
		_REGISTRY.__init__(self)
		self.name = "REGISTRIES"
		self.specie = 'nouns'
		self.basic = "registry"
		self.jsondata = {}
