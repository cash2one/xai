

from xai.brain.wordbase.verbs._mislay import _MISLAY

#calss header
class _MISLAID(_MISLAY, ):
	def __init__(self,): 
		_MISLAY.__init__(self)
		self.name = "MISLAID"
		self.specie = 'verbs'
		self.basic = "mislay"
		self.jsondata = {}
