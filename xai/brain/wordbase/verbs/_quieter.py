

from xai.brain.wordbase.verbs._quiet import _QUIET

#calss header
class _QUIETER(_QUIET, ):
	def __init__(self,): 
		_QUIET.__init__(self)
		self.name = "QUIETER"
		self.specie = 'verbs'
		self.basic = "quiet"
		self.jsondata = {}
