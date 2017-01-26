

from xai.brain.wordbase.adjectives._veterinary import _VETERINARY

#calss header
class _VETERINARIES(_VETERINARY, ):
	def __init__(self,): 
		_VETERINARY.__init__(self)
		self.name = "VETERINARIES"
		self.specie = 'adjectives'
		self.basic = "veterinary"
		self.jsondata = {}
