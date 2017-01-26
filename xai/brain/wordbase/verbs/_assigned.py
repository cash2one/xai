

from xai.brain.wordbase.verbs._assign import _ASSIGN

#calss header
class _ASSIGNED(_ASSIGN, ):
	def __init__(self,): 
		_ASSIGN.__init__(self)
		self.name = "ASSIGNED"
		self.specie = 'verbs'
		self.basic = "assign"
		self.jsondata = {}
