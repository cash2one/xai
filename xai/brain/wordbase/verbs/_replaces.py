

from xai.brain.wordbase.verbs._replace import _REPLACE

#calss header
class _REPLACES(_REPLACE, ):
	def __init__(self,): 
		_REPLACE.__init__(self)
		self.name = "REPLACES"
		self.specie = 'verbs'
		self.basic = "replace"
		self.jsondata = {}
