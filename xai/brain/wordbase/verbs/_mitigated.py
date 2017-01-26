

from xai.brain.wordbase.verbs._mitigate import _MITIGATE

#calss header
class _MITIGATED(_MITIGATE, ):
	def __init__(self,): 
		_MITIGATE.__init__(self)
		self.name = "MITIGATED"
		self.specie = 'verbs'
		self.basic = "mitigate"
		self.jsondata = {}
