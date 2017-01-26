

from xai.brain.wordbase.nouns._override import _OVERRIDE

#calss header
class _OVERRIDDEN(_OVERRIDE, ):
	def __init__(self,): 
		_OVERRIDE.__init__(self)
		self.name = "OVERRIDDEN"
		self.specie = 'nouns'
		self.basic = "override"
		self.jsondata = {}
