

from xai.brain.wordbase.verbs._caution import _CAUTION

#calss header
class _CAUTIONED(_CAUTION, ):
	def __init__(self,): 
		_CAUTION.__init__(self)
		self.name = "CAUTIONED"
		self.specie = 'verbs'
		self.basic = "caution"
		self.jsondata = {}
