

from xai.brain.wordbase.adjectives._compound import _COMPOUND

#calss header
class _COMPOUNDING(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDING"
		self.specie = 'adjectives'
		self.basic = "compound"
		self.jsondata = {}
