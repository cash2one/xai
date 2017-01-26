

from xai.brain.wordbase.verbs._audit import _AUDIT

#calss header
class _AUDITED(_AUDIT, ):
	def __init__(self,): 
		_AUDIT.__init__(self)
		self.name = "AUDITED"
		self.specie = 'verbs'
		self.basic = "audit"
		self.jsondata = {}
