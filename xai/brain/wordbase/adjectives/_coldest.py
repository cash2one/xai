

from xai.brain.wordbase.adjectives._cold import _COLD

#calss header
class _COLDEST(_COLD, ):
	def __init__(self,): 
		_COLD.__init__(self)
		self.name = "COLDEST"
		self.specie = 'adjectives'
		self.basic = "cold"
		self.jsondata = {}
