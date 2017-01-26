

from xai.brain.wordbase.verbs._discuss import _DISCUSS

#calss header
class _DISCUSSED(_DISCUSS, ):
	def __init__(self,): 
		_DISCUSS.__init__(self)
		self.name = "DISCUSSED"
		self.specie = 'verbs'
		self.basic = "discuss"
		self.jsondata = {}
