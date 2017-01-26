

from xai.brain.wordbase.nouns._dummy import _DUMMY

#calss header
class _DUMMIES(_DUMMY, ):
	def __init__(self,): 
		_DUMMY.__init__(self)
		self.name = "DUMMIES"
		self.specie = 'nouns'
		self.basic = "dummy"
		self.jsondata = {}
