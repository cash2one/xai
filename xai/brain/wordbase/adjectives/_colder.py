

from xai.brain.wordbase.adjectives._cold import _COLD

#calss header
class _COLDER(_COLD, ):
	def __init__(self,): 
		_COLD.__init__(self)
		self.name = "COLDER"
		self.specie = 'adjectives'
		self.basic = "cold"
		self.jsondata = {}
