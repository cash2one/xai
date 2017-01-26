

from xai.brain.wordbase.verbs._brand import _BRAND

#calss header
class _BRANDS(_BRAND, ):
	def __init__(self,): 
		_BRAND.__init__(self)
		self.name = "BRANDS"
		self.specie = 'verbs'
		self.basic = "brand"
		self.jsondata = {}
