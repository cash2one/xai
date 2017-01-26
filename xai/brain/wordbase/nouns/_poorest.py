

from xai.brain.wordbase.nouns._poor import _POOR

#calss header
class _POOREST(_POOR, ):
	def __init__(self,): 
		_POOR.__init__(self)
		self.name = "POOREST"
		self.specie = 'nouns'
		self.basic = "poor"
		self.jsondata = {}
