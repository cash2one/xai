

from xai.brain.wordbase.verbs._outrank import _OUTRANK

#calss header
class _OUTRANKED(_OUTRANK, ):
	def __init__(self,): 
		_OUTRANK.__init__(self)
		self.name = "OUTRANKED"
		self.specie = 'verbs'
		self.basic = "outrank"
		self.jsondata = {}
