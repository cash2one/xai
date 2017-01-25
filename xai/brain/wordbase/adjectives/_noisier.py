

from xai.brain.wordbase.adjectives._noisy import _NOISY

#calss header
class _NOISIER(_NOISY, ):
	def __init__(self,): 
		_NOISY.__init__(self)
		self.name = "NOISIER"
		self.specie = 'adjectives'
		self.basic = "noisy"
		self.jsondata = {}
