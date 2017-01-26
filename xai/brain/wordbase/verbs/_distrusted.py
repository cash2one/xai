

from xai.brain.wordbase.verbs._distrust import _DISTRUST

#calss header
class _DISTRUSTED(_DISTRUST, ):
	def __init__(self,): 
		_DISTRUST.__init__(self)
		self.name = "DISTRUSTED"
		self.specie = 'verbs'
		self.basic = "distrust"
		self.jsondata = {}
