

from xai.brain.wordbase.verbs._admit import _ADMIT

#calss header
class _ADMITTED(_ADMIT, ):
	def __init__(self,): 
		_ADMIT.__init__(self)
		self.name = "ADMITTED"
		self.specie = 'verbs'
		self.basic = "admit"
		self.jsondata = {}
