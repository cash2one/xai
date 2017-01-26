

from xai.brain.wordbase.nouns._shipment import _SHIPMENT

#calss header
class _SHIPMENTS(_SHIPMENT, ):
	def __init__(self,): 
		_SHIPMENT.__init__(self)
		self.name = "SHIPMENTS"
		self.specie = 'nouns'
		self.basic = "shipment"
		self.jsondata = {}
