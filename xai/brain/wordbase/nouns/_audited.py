

from xai.brain.wordbase.nouns._audit import _AUDIT

#calss header
class _AUDITED(_AUDIT, ):
	def __init__(self,): 
		_AUDIT.__init__(self)
		self.name = "AUDITED"
		self.specie = 'nouns'
		self.basic = "audit"
		self.jsondata = {}
