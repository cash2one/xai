

from xai.brain.wordbase.verbs._broker import _BROKER

#calss header
class _BROKERED(_BROKER, ):
	def __init__(self,): 
		_BROKER.__init__(self)
		self.name = "BROKERED"
		self.specie = 'verbs'
		self.basic = "broker"
		self.jsondata = {}
