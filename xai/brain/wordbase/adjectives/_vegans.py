

from xai.brain.wordbase.adjectives._vegan import _VEGAN

#calss header
class _VEGANS(_VEGAN, ):
	def __init__(self,): 
		_VEGAN.__init__(self)
		self.name = "VEGANS"
		self.specie = 'adjectives'
		self.basic = "vegan"
		self.jsondata = {}
