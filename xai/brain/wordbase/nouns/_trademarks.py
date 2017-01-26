

from xai.brain.wordbase.nouns._trademark import _TRADEMARK

#calss header
class _TRADEMARKS(_TRADEMARK, ):
	def __init__(self,): 
		_TRADEMARK.__init__(self)
		self.name = "TRADEMARKS"
		self.specie = 'nouns'
		self.basic = "trademark"
		self.jsondata = {}
