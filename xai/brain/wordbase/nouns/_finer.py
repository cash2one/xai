

from xai.brain.wordbase.nouns._fine import _FINE

#calss header
class _FINER(_FINE, ):
	def __init__(self,): 
		_FINE.__init__(self)
		self.name = "FINER"
		self.specie = 'nouns'
		self.basic = "fine"
		self.jsondata = {}
