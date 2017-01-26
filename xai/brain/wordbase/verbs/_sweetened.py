

from xai.brain.wordbase.verbs._sweeten import _SWEETEN

#calss header
class _SWEETENED(_SWEETEN, ):
	def __init__(self,): 
		_SWEETEN.__init__(self)
		self.name = "SWEETENED"
		self.specie = 'verbs'
		self.basic = "sweeten"
		self.jsondata = {}
