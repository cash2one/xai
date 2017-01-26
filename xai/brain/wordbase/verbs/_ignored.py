

from xai.brain.wordbase.verbs._ignore import _IGNORE

#calss header
class _IGNORED(_IGNORE, ):
	def __init__(self,): 
		_IGNORE.__init__(self)
		self.name = "IGNORED"
		self.specie = 'verbs'
		self.basic = "ignore"
		self.jsondata = {}
