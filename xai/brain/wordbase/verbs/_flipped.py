

from xai.brain.wordbase.verbs._flip import _FLIP

#calss header
class _FLIPPED(_FLIP, ):
	def __init__(self,): 
		_FLIP.__init__(self)
		self.name = "FLIPPED"
		self.specie = 'verbs'
		self.basic = "flip"
		self.jsondata = {}
