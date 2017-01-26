

from xai.brain.wordbase.adjectives._real import _REAL

#calss header
class _REALS(_REAL, ):
	def __init__(self,): 
		_REAL.__init__(self)
		self.name = "REALS"
		self.specie = 'adjectives'
		self.basic = "real"
		self.jsondata = {}
