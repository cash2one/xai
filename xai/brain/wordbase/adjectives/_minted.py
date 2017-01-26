

from xai.brain.wordbase.adjectives._mint import _MINT

#calss header
class _MINTED(_MINT, ):
	def __init__(self,): 
		_MINT.__init__(self)
		self.name = "MINTED"
		self.specie = 'adjectives'
		self.basic = "mint"
		self.jsondata = {}
