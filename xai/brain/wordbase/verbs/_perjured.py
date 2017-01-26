

from xai.brain.wordbase.verbs._perjure import _PERJURE

#calss header
class _PERJURED(_PERJURE, ):
	def __init__(self,): 
		_PERJURE.__init__(self)
		self.name = "PERJURED"
		self.specie = 'verbs'
		self.basic = "perjure"
		self.jsondata = {}
