

from xai.brain.wordbase.adjectives._poor import _POOR

#calss header
class _POOREST(_POOR, ):
	def __init__(self,): 
		_POOR.__init__(self)
		self.name = "POOREST"
		self.specie = 'adjectives'
		self.basic = "poor"
		self.jsondata = {}
