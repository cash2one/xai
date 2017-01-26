

from xai.brain.wordbase.adjectives._dummy import _DUMMY

#calss header
class _DUMMIES(_DUMMY, ):
	def __init__(self,): 
		_DUMMY.__init__(self)
		self.name = "DUMMIES"
		self.specie = 'adjectives'
		self.basic = "dummy"
		self.jsondata = {}
