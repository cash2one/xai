

from xai.brain.wordbase.verbs._confound import _CONFOUND

#calss header
class _CONFOUNDING(_CONFOUND, ):
	def __init__(self,): 
		_CONFOUND.__init__(self)
		self.name = "CONFOUNDING"
		self.specie = 'verbs'
		self.basic = "confound"
		self.jsondata = {}
