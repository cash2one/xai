

from xai.brain.wordbase.nouns._decay import _DECAY

#calss header
class _DECAYED(_DECAY, ):
	def __init__(self,): 
		_DECAY.__init__(self)
		self.name = "DECAYED"
		self.specie = 'nouns'
		self.basic = "decay"
		self.jsondata = {}
