

from xai.brain.wordbase.verbs._salute import _SALUTE

#calss header
class _SALUTED(_SALUTE, ):
	def __init__(self,): 
		_SALUTE.__init__(self)
		self.name = "SALUTED"
		self.specie = 'verbs'
		self.basic = "salute"
		self.jsondata = {}
