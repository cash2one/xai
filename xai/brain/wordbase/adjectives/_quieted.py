

from xai.brain.wordbase.adjectives._quiet import _QUIET

#calss header
class _QUIETED(_QUIET, ):
	def __init__(self,): 
		_QUIET.__init__(self)
		self.name = "QUIETED"
		self.specie = 'adjectives'
		self.basic = "quiet"
		self.jsondata = {}
