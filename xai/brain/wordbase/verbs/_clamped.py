

from xai.brain.wordbase.verbs._clamp import _CLAMP

#calss header
class _CLAMPED(_CLAMP, ):
	def __init__(self,): 
		_CLAMP.__init__(self)
		self.name = "CLAMPED"
		self.specie = 'verbs'
		self.basic = "clamp"
		self.jsondata = {}
