

from xai.brain.wordbase.adjectives._professional import _PROFESSIONAL

#calss header
class _PROFESSIONALS(_PROFESSIONAL, ):
	def __init__(self,): 
		_PROFESSIONAL.__init__(self)
		self.name = "PROFESSIONALS"
		self.specie = 'adjectives'
		self.basic = "professional"
		self.jsondata = {}
