

from xai.brain.wordbase.nouns._brand import _BRAND

#calss header
class _BRANDS(_BRAND, ):
	def __init__(self,): 
		_BRAND.__init__(self)
		self.name = "BRANDS"
		self.specie = 'nouns'
		self.basic = "brand"
		self.jsondata = {}
