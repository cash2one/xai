

from xai.brain.wordbase.verbs._evaluate import _EVALUATE

#calss header
class _EVALUATED(_EVALUATE, ):
	def __init__(self,): 
		_EVALUATE.__init__(self)
		self.name = "EVALUATED"
		self.specie = 'verbs'
		self.basic = "evaluate"
		self.jsondata = {}
