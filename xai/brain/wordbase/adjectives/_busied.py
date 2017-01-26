

from xai.brain.wordbase.adjectives._busy import _BUSY

#calss header
class _BUSIED(_BUSY, ):
	def __init__(self,): 
		_BUSY.__init__(self)
		self.name = "BUSIED"
		self.specie = 'adjectives'
		self.basic = "busy"
		self.jsondata = {}
