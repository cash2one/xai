

from xai.brain.wordbase.verbs._override import _OVERRIDE

#calss header
class _OVERRIDDEN(_OVERRIDE, ):
	def __init__(self,): 
		_OVERRIDE.__init__(self)
		self.name = "OVERRIDDEN"
		self.specie = 'verbs'
		self.basic = "override"
		self.jsondata = {}
