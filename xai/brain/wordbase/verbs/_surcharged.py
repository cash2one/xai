

from xai.brain.wordbase.verbs._surcharge import _SURCHARGE

#calss header
class _SURCHARGED(_SURCHARGE, ):
	def __init__(self,): 
		_SURCHARGE.__init__(self)
		self.name = "SURCHARGED"
		self.specie = 'verbs'
		self.basic = "surcharge"
		self.jsondata = {}
