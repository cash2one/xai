

from xai.brain.wordbase.nouns._squelch import _SQUELCH

#calss header
class _SQUELCHED(_SQUELCH, ):
	def __init__(self,): 
		_SQUELCH.__init__(self)
		self.name = "SQUELCHED"
		self.specie = 'nouns'
		self.basic = "squelch"
		self.jsondata = {}
