

from xai.brain.wordbase.nouns._flip import _FLIP

#calss header
class _FLIPPED(_FLIP, ):
	def __init__(self,): 
		_FLIP.__init__(self)
		self.name = "FLIPPED"
		self.specie = 'nouns'
		self.basic = "flip"
		self.jsondata = {}
