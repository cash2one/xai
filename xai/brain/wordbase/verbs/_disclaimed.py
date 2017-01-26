

from xai.brain.wordbase.verbs._disclaim import _DISCLAIM

#calss header
class _DISCLAIMED(_DISCLAIM, ):
	def __init__(self,): 
		_DISCLAIM.__init__(self)
		self.name = "DISCLAIMED"
		self.specie = 'verbs'
		self.basic = "disclaim"
		self.jsondata = {}
