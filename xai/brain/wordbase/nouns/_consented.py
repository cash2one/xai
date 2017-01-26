

from xai.brain.wordbase.nouns._consent import _CONSENT

#calss header
class _CONSENTED(_CONSENT, ):
	def __init__(self,): 
		_CONSENT.__init__(self)
		self.name = "CONSENTED"
		self.specie = 'nouns'
		self.basic = "consent"
		self.jsondata = {}
