

from xai.brain.wordbase.verbs._unmask import _UNMASK

#calss header
class _UNMASKED(_UNMASK, ):
	def __init__(self,): 
		_UNMASK.__init__(self)
		self.name = "UNMASKED"
		self.specie = 'verbs'
		self.basic = "unmask"
		self.jsondata = {}
