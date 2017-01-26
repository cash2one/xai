

from xai.brain.wordbase.adjectives._gross import _GROSS

#calss header
class _GROSSED(_GROSS, ):
	def __init__(self,): 
		_GROSS.__init__(self)
		self.name = "GROSSED"
		self.specie = 'adjectives'
		self.basic = "gross"
		self.jsondata = {}
