

from xai.brain.wordbase.nouns._censor import _CENSOR

#calss header
class _CENSORED(_CENSOR, ):
	def __init__(self,): 
		_CENSOR.__init__(self)
		self.name = "CENSORED"
		self.specie = 'nouns'
		self.basic = "censor"
		self.jsondata = {}
