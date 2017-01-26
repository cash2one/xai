

from xai.brain.wordbase.verbs._quiet import _QUIET

#calss header
class _QUIETED(_QUIET, ):
	def __init__(self,): 
		_QUIET.__init__(self)
		self.name = "QUIETED"
		self.specie = 'verbs'
		self.basic = "quiet"
		self.jsondata = {}
