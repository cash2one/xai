

from xai.brain.wordbase.verbs._mint import _MINT

#calss header
class _MINTED(_MINT, ):
	def __init__(self,): 
		_MINT.__init__(self)
		self.name = "MINTED"
		self.specie = 'verbs'
		self.basic = "mint"
		self.jsondata = {}
