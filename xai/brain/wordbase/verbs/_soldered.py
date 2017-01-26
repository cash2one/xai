

from xai.brain.wordbase.verbs._solder import _SOLDER

#calss header
class _SOLDERED(_SOLDER, ):
	def __init__(self,): 
		_SOLDER.__init__(self)
		self.name = "SOLDERED"
		self.specie = 'verbs'
		self.basic = "solder"
		self.jsondata = {}
