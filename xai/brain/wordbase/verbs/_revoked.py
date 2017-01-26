

from xai.brain.wordbase.verbs._revoke import _REVOKE

#calss header
class _REVOKED(_REVOKE, ):
	def __init__(self,): 
		_REVOKE.__init__(self)
		self.name = "REVOKED"
		self.specie = 'verbs'
		self.basic = "revoke"
		self.jsondata = {}
