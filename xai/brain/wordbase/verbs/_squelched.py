

from xai.brain.wordbase.verbs._squelch import _SQUELCH

#calss header
class _SQUELCHED(_SQUELCH, ):
	def __init__(self,): 
		_SQUELCH.__init__(self)
		self.name = "SQUELCHED"
		self.specie = 'verbs'
		self.basic = "squelch"
		self.jsondata = {}
