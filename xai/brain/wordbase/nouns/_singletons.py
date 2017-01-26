

from xai.brain.wordbase.nouns._singleton import _SINGLETON

#calss header
class _SINGLETONS(_SINGLETON, ):
	def __init__(self,): 
		_SINGLETON.__init__(self)
		self.name = "SINGLETONS"
		self.specie = 'nouns'
		self.basic = "singleton"
		self.jsondata = {}
