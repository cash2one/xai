

from xai.brain.wordbase.verbs._correct import _CORRECT

#calss header
class _CORRECTED(_CORRECT, ):
	def __init__(self,): 
		_CORRECT.__init__(self)
		self.name = "CORRECTED"
		self.specie = 'verbs'
		self.basic = "correct"
		self.jsondata = {}
