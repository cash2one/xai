

from xai.brain.wordbase.verbs._imprint import _IMPRINT

#calss header
class _IMPRINTED(_IMPRINT, ):
	def __init__(self,): 
		_IMPRINT.__init__(self)
		self.name = "IMPRINTED"
		self.specie = 'verbs'
		self.basic = "imprint"
		self.jsondata = {}
