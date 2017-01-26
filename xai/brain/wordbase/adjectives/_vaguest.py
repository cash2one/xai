

from xai.brain.wordbase.adjectives._vague import _VAGUE

#calss header
class _VAGUEST(_VAGUE, ):
	def __init__(self,): 
		_VAGUE.__init__(self)
		self.name = "VAGUEST"
		self.specie = 'adjectives'
		self.basic = "vague"
		self.jsondata = {}
