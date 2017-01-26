

from xai.brain.wordbase.verbs._provision import _PROVISION

#calss header
class _PROVISIONED(_PROVISION, ):
	def __init__(self,): 
		_PROVISION.__init__(self)
		self.name = "PROVISIONED"
		self.specie = 'verbs'
		self.basic = "provision"
		self.jsondata = {}
