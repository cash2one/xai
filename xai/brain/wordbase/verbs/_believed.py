

from xai.brain.wordbase.verbs._believe import _BELIEVE

#calss header
class _BELIEVED(_BELIEVE, ):
	def __init__(self,): 
		_BELIEVE.__init__(self)
		self.name = "BELIEVED"
		self.specie = 'verbs'
		self.basic = "believe"
		self.jsondata = {}
