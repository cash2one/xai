

from xai.brain.wordbase.nouns._shop import _SHOP

#calss header
class _SHOPPED(_SHOP, ):
	def __init__(self,): 
		_SHOP.__init__(self)
		self.name = "SHOPPED"
		self.specie = 'nouns'
		self.basic = "shop"
		self.jsondata = {}
