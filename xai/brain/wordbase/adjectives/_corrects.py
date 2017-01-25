

from xai.brain.wordbase.adjectives._correct import _CORRECT

#calss header
class _CORRECTS(_CORRECT, ):
	def __init__(self,): 
		_CORRECT.__init__(self)
		self.name = "CORRECTS"
		self.specie = 'adjectives'
		self.basic = "correct"
		self.jsondata = {}
