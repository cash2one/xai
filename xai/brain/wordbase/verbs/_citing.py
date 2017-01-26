

from xai.brain.wordbase.verbs._cite import _CITE

#calss header
class _CITING(_CITE, ):
	def __init__(self,): 
		_CITE.__init__(self)
		self.name = "CITING"
		self.specie = 'verbs'
		self.basic = "cite"
		self.jsondata = {}
