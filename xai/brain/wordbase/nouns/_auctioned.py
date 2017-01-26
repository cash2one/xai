

from xai.brain.wordbase.nouns._auction import _AUCTION

#calss header
class _AUCTIONED(_AUCTION, ):
	def __init__(self,): 
		_AUCTION.__init__(self)
		self.name = "AUCTIONED"
		self.specie = 'nouns'
		self.basic = "auction"
		self.jsondata = {}
