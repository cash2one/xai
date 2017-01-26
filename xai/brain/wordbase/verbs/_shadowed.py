

from xai.brain.wordbase.verbs._shadow import _SHADOW

#calss header
class _SHADOWED(_SHADOW, ):
	def __init__(self,): 
		_SHADOW.__init__(self)
		self.name = "SHADOWED"
		self.specie = 'verbs'
		self.basic = "shadow"
		self.jsondata = {}
