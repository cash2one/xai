

from xai.brain.wordbase.nouns._customer import _CUSTOMER

#calss header
class _CUSTOMERS(_CUSTOMER, ):
	def __init__(self,): 
		_CUSTOMER.__init__(self)
		self.name = "CUSTOMERS"
		self.specie = 'nouns'
		self.basic = "customer"
		self.jsondata = {}
