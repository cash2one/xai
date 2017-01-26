

from xai.brain.wordbase.adjectives._compound import _COMPOUND

#calss header
class _COMPOUNDS(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDS"
		self.specie = 'adjectives'
		self.basic = "compound"
		self.jsondata = {}
