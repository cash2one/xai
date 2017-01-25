

from xai.brain.wordbase.adjectives._bold import _BOLD

#calss header
class _BOLDER(_BOLD, ):
	def __init__(self,): 
		_BOLD.__init__(self)
		self.name = "BOLDER"
		self.specie = 'adjectives'
		self.basic = "bold"
		self.jsondata = {}
