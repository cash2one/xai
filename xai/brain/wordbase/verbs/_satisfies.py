

from xai.brain.wordbase.verbs._satisfy import _SATISFY

#calss header
class _SATISFIES(_SATISFY, ):
	def __init__(self,): 
		_SATISFY.__init__(self)
		self.name = "SATISFIES"
		self.specie = 'verbs'
		self.basic = "satisfy"
		self.jsondata = {}
