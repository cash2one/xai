

from xai.brain.wordbase.adjectives._correct import _CORRECT

#calss header
class _CORRECTED(_CORRECT, ):
	def __init__(self,): 
		_CORRECT.__init__(self)
		self.name = "CORRECTED"
		self.specie = 'adjectives'
		self.basic = "correct"
		self.jsondata = {}
