

from xai.brain.wordbase.verbs._invert import _INVERT

#calss header
class _INVERTED(_INVERT, ):
	def __init__(self,): 
		_INVERT.__init__(self)
		self.name = "INVERTED"
		self.specie = 'verbs'
		self.basic = "invert"
		self.jsondata = {}
