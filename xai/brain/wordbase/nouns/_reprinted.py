

from xai.brain.wordbase.nouns._reprint import _REPRINT

#calss header
class _REPRINTED(_REPRINT, ):
	def __init__(self,): 
		_REPRINT.__init__(self)
		self.name = "REPRINTED"
		self.specie = 'nouns'
		self.basic = "reprint"
		self.jsondata = {}
