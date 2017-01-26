

from xai.brain.wordbase.verbs._deny import _DENY

#calss header
class _DENIED(_DENY, ):
	def __init__(self,): 
		_DENY.__init__(self)
		self.name = "DENIED"
		self.specie = 'verbs'
		self.basic = "deny"
		self.jsondata = {}
