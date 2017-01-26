

from xai.brain.wordbase.verbs._consume import _CONSUME

#calss header
class _CONSUMES(_CONSUME, ):
	def __init__(self,): 
		_CONSUME.__init__(self)
		self.name = "CONSUMES"
		self.specie = 'verbs'
		self.basic = "consume"
		self.jsondata = {}
