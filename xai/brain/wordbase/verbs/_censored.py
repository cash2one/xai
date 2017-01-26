

from xai.brain.wordbase.verbs._censor import _CENSOR

#calss header
class _CENSORED(_CENSOR, ):
	def __init__(self,): 
		_CENSOR.__init__(self)
		self.name = "CENSORED"
		self.specie = 'verbs'
		self.basic = "censor"
		self.jsondata = {}
