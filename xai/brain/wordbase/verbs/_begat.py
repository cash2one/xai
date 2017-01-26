

from xai.brain.wordbase.verbs._beget import _BEGET

#calss header
class _BEGAT(_BEGET, ):
	def __init__(self,): 
		_BEGET.__init__(self)
		self.name = "BEGAT"
		self.specie = 'verbs'
		self.basic = "beget"
		self.jsondata = {}
