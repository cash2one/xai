

from xai.brain.wordbase.adjectives._exclusive import _EXCLUSIVE

#calss header
class _EXCLUSIVES(_EXCLUSIVE, ):
	def __init__(self,): 
		_EXCLUSIVE.__init__(self)
		self.name = "EXCLUSIVES"
		self.specie = 'adjectives'
		self.basic = "exclusive"
		self.jsondata = {}
