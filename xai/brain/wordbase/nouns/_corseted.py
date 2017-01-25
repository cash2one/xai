

from xai.brain.wordbase.nouns._corset import _CORSET

#calss header
class _CORSETED(_CORSET, ):
	def __init__(self,): 
		_CORSET.__init__(self)
		self.name = "CORSETED"
		self.specie = 'nouns'
		self.basic = "corset"
		self.jsondata = {}
