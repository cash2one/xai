

from xai.brain.wordbase.verbs._eavesdrop import _EAVESDROP

#calss header
class _EAVESDROPPED(_EAVESDROP, ):
	def __init__(self,): 
		_EAVESDROP.__init__(self)
		self.name = "EAVESDROPPED"
		self.specie = 'verbs'
		self.basic = "eavesdrop"
		self.jsondata = {}
