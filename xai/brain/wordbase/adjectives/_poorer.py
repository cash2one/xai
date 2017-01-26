

from xai.brain.wordbase.adjectives._poor import _POOR

#calss header
class _POORER(_POOR, ):
	def __init__(self,): 
		_POOR.__init__(self)
		self.name = "POORER"
		self.specie = 'adjectives'
		self.basic = "poor"
		self.jsondata = {}
