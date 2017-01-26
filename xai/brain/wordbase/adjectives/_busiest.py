

from xai.brain.wordbase.adjectives._busy import _BUSY

#calss header
class _BUSIEST(_BUSY, ):
	def __init__(self,): 
		_BUSY.__init__(self)
		self.name = "BUSIEST"
		self.specie = 'adjectives'
		self.basic = "busy"
		self.jsondata = {}
