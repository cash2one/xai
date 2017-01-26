

from xai.brain.wordbase.adjectives._spare import _SPARE

#calss header
class _SPARES(_SPARE, ):
	def __init__(self,): 
		_SPARE.__init__(self)
		self.name = "SPARES"
		self.specie = 'adjectives'
		self.basic = "spare"
		self.jsondata = {}
