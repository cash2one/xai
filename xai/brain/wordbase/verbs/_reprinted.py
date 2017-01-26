

from xai.brain.wordbase.verbs._reprint import _REPRINT

#calss header
class _REPRINTED(_REPRINT, ):
	def __init__(self,): 
		_REPRINT.__init__(self)
		self.name = "REPRINTED"
		self.specie = 'verbs'
		self.basic = "reprint"
		self.jsondata = {}
