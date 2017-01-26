

from xai.brain.wordbase.verbs._defrost import _DEFROST

#calss header
class _DEFROSTED(_DEFROST, ):
	def __init__(self,): 
		_DEFROST.__init__(self)
		self.name = "DEFROSTED"
		self.specie = 'verbs'
		self.basic = "defrost"
		self.jsondata = {}
