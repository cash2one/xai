

from xai.brain.wordbase.verbs._salute import _SALUTE

#calss header
class _SALUTING(_SALUTE, ):
	def __init__(self,): 
		_SALUTE.__init__(self)
		self.name = "SALUTING"
		self.specie = 'verbs'
		self.basic = "salute"
		self.jsondata = {}
