

from xai.brain.wordbase.verbs._consent import _CONSENT

#calss header
class _CONSENTING(_CONSENT, ):
	def __init__(self,): 
		_CONSENT.__init__(self)
		self.name = "CONSENTING"
		self.specie = 'verbs'
		self.basic = "consent"
		self.jsondata = {}
