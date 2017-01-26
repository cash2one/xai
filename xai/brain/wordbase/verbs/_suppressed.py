

from xai.brain.wordbase.verbs._suppress import _SUPPRESS

#calss header
class _SUPPRESSED(_SUPPRESS, ):
	def __init__(self,): 
		_SUPPRESS.__init__(self)
		self.name = "SUPPRESSED"
		self.specie = 'verbs'
		self.basic = "suppress"
		self.jsondata = {}
