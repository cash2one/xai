

from xai.brain.wordbase.adverbs._fine import _FINE

#calss header
class _FINER(_FINE, ):
	def __init__(self,): 
		_FINE.__init__(self)
		self.name = "FINER"
		self.specie = 'adverbs'
		self.basic = "fine"
		self.jsondata = {}
