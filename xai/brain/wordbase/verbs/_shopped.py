

from xai.brain.wordbase.verbs._shop import _SHOP

#calss header
class _SHOPPED(_SHOP, ):
	def __init__(self,): 
		_SHOP.__init__(self)
		self.name = "SHOPPED"
		self.specie = 'verbs'
		self.basic = "shop"
		self.jsondata = {}
