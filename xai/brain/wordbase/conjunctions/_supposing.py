

from xai.brain.wordbase.conjunctions._suppose import _SUPPOSE

#calss header
class _SUPPOSING(_SUPPOSE, ):
	def __init__(self,): 
		_SUPPOSE.__init__(self)
		self.name = "SUPPOSING"
		self.specie = 'conjunctions'
		self.basic = "suppose"
		self.jsondata = {}
