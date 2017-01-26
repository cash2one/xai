

from xai.brain.wordbase.verbs._suspend import _SUSPEND

#calss header
class _SUSPENDED(_SUSPEND, ):
	def __init__(self,): 
		_SUSPEND.__init__(self)
		self.name = "SUSPENDED"
		self.specie = 'verbs'
		self.basic = "suspend"
		self.jsondata = {}
