

from xai.brain.wordbase.verbs._auction import _AUCTION

#calss header
class _AUCTIONED(_AUCTION, ):
	def __init__(self,): 
		_AUCTION.__init__(self)
		self.name = "AUCTIONED"
		self.specie = 'verbs'
		self.basic = "auction"
		self.jsondata = {}
