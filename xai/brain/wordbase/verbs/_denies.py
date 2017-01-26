

from xai.brain.wordbase.verbs._deny import _DENY

#calss header
class _DENIES(_DENY, ):
	def __init__(self,): 
		_DENY.__init__(self)
		self.name = "DENIES"
		self.specie = 'verbs'
		self.basic = "deny"
		self.jsondata = {}
