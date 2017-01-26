

from xai.brain.wordbase.verbs._soap import _SOAP

#calss header
class _SOAPS(_SOAP, ):
	def __init__(self,): 
		_SOAP.__init__(self)
		self.name = "SOAPS"
		self.specie = 'verbs'
		self.basic = "soap"
		self.jsondata = {}
