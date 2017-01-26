

from xai.brain.wordbase.adjectives._compound import _COMPOUND

#calss header
class _COMPOUNDED(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDED"
		self.specie = 'adjectives'
		self.basic = "compound"
		self.jsondata = {}
