

from xai.brain.wordbase.verbs._confound import _CONFOUND

#calss header
class _CONFOUNDS(_CONFOUND, ):
	def __init__(self,): 
		_CONFOUND.__init__(self)
		self.name = "CONFOUNDS"
		self.specie = 'verbs'
		self.basic = "confound"
		self.jsondata = {}
