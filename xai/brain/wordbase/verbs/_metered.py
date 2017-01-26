

from xai.brain.wordbase.verbs._meter import _METER

#calss header
class _METERED(_METER, ):
	def __init__(self,): 
		_METER.__init__(self)
		self.name = "METERED"
		self.specie = 'verbs'
		self.basic = "meter"
		self.jsondata = {}
