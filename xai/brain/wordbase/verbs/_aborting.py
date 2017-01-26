

from xai.brain.wordbase.verbs._abort import _ABORT

#calss header
class _ABORTING(_ABORT, ):
	def __init__(self,): 
		_ABORT.__init__(self)
		self.name = "ABORTING"
		self.specie = 'verbs'
		self.basic = "abort"
		self.jsondata = {}
