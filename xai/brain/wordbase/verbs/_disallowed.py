

from xai.brain.wordbase.verbs._disallow import _DISALLOW

#calss header
class _DISALLOWED(_DISALLOW, ):
	def __init__(self,): 
		_DISALLOW.__init__(self)
		self.name = "DISALLOWED"
		self.specie = 'verbs'
		self.basic = "disallow"
		self.jsondata = {}
