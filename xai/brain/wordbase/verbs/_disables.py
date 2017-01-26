

from xai.brain.wordbase.verbs._disable import _DISABLE

#calss header
class _DISABLES(_DISABLE, ):
	def __init__(self,): 
		_DISABLE.__init__(self)
		self.name = "DISABLES"
		self.specie = 'verbs'
		self.basic = "disable"
		self.jsondata = {}
