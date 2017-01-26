

from xai.brain.wordbase.adjectives._gray import _GRAY

#calss header
class _GRAYER(_GRAY, ):
	def __init__(self,): 
		_GRAY.__init__(self)
		self.name = "GRAYER"
		self.specie = 'adjectives'
		self.basic = "gray"
		self.jsondata = {}
