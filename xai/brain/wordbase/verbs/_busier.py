

from xai.brain.wordbase.verbs._busy import _BUSY

#calss header
class _BUSIER(_BUSY, ):
	def __init__(self,): 
		_BUSY.__init__(self)
		self.name = "BUSIER"
		self.specie = 'verbs'
		self.basic = "busy"
		self.jsondata = {}
