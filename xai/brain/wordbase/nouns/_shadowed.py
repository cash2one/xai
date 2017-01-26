

from xai.brain.wordbase.nouns._shadow import _SHADOW

#calss header
class _SHADOWED(_SHADOW, ):
	def __init__(self,): 
		_SHADOW.__init__(self)
		self.name = "SHADOWED"
		self.specie = 'nouns'
		self.basic = "shadow"
		self.jsondata = {}
