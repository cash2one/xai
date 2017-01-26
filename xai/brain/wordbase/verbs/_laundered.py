

from xai.brain.wordbase.verbs._launder import _LAUNDER

#calss header
class _LAUNDERED(_LAUNDER, ):
	def __init__(self,): 
		_LAUNDER.__init__(self)
		self.name = "LAUNDERED"
		self.specie = 'verbs'
		self.basic = "launder"
		self.jsondata = {}
