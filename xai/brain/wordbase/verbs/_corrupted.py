

from xai.brain.wordbase.verbs._corrupt import _CORRUPT

#calss header
class _CORRUPTED(_CORRUPT, ):
	def __init__(self,): 
		_CORRUPT.__init__(self)
		self.name = "CORRUPTED"
		self.specie = 'verbs'
		self.basic = "corrupt"
		self.jsondata = {}
