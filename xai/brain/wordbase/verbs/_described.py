

from xai.brain.wordbase.verbs._describe import _DESCRIBE

#calss header
class _DESCRIBED(_DESCRIBE, ):
	def __init__(self,): 
		_DESCRIBE.__init__(self)
		self.name = "DESCRIBED"
		self.specie = 'verbs'
		self.basic = "describe"
		self.jsondata = {}
