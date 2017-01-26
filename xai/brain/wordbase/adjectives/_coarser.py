

from xai.brain.wordbase.adjectives._coarse import _COARSE

#calss header
class _COARSER(_COARSE, ):
	def __init__(self,): 
		_COARSE.__init__(self)
		self.name = "COARSER"
		self.specie = 'adjectives'
		self.basic = "coarse"
		self.jsondata = {}
