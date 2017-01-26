

from xai.brain.wordbase.verbs._dummy import _DUMMY

#calss header
class _DUMMIES(_DUMMY, ):
	def __init__(self,): 
		_DUMMY.__init__(self)
		self.name = "DUMMIES"
		self.specie = 'verbs'
		self.basic = "dummy"
		self.jsondata = {}
