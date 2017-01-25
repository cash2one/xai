

from xai.brain.wordbase.nouns._consent import _CONSENT

#calss header
class _CONSENTING(_CONSENT, ):
	def __init__(self,): 
		_CONSENT.__init__(self)
		self.name = "CONSENTING"
		self.specie = 'nouns'
		self.basic = "consent"
		self.jsondata = {}
