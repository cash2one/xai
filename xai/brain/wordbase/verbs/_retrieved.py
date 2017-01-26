

from xai.brain.wordbase.verbs._retrieve import _RETRIEVE

#calss header
class _RETRIEVED(_RETRIEVE, ):
	def __init__(self,): 
		_RETRIEVE.__init__(self)
		self.name = "RETRIEVED"
		self.specie = 'verbs'
		self.basic = "retrieve"
		self.jsondata = {}
