

from xai.brain.wordbase.nouns._broker import _BROKER

#calss header
class _BROKERED(_BROKER, ):
	def __init__(self,): 
		_BROKER.__init__(self)
		self.name = "BROKERED"
		self.specie = 'nouns'
		self.basic = "broker"
		self.jsondata = {}
