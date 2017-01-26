

from xai.brain.wordbase.nouns._fuel import _FUEL

#calss header
class _FUELLED(_FUEL, ):
	def __init__(self,): 
		_FUEL.__init__(self)
		self.name = "FUELLED"
		self.specie = 'nouns'
		self.basic = "fuel"
		self.jsondata = {}
