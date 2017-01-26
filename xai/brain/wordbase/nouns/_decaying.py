

from xai.brain.wordbase.nouns._decay import _DECAY

#calss header
class _DECAYING(_DECAY, ):
	def __init__(self,): 
		_DECAY.__init__(self)
		self.name = "DECAYING"
		self.specie = 'nouns'
		self.basic = "decay"
		self.jsondata = {}
