

from xai.brain.wordbase.nouns._purchase import _PURCHASE

#calss header
class _PURCHASED(_PURCHASE, ):
	def __init__(self,): 
		_PURCHASE.__init__(self)
		self.name = "PURCHASED"
		self.specie = 'nouns'
		self.basic = "purchase"
		self.jsondata = {}
