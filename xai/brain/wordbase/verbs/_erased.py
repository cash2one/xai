

from xai.brain.wordbase.verbs._erase import _ERASE

#calss header
class _ERASED(_ERASE, ):
	def __init__(self,): 
		_ERASE.__init__(self)
		self.name = "ERASED"
		self.specie = 'verbs'
		self.basic = "erase"
		self.jsondata = {}
