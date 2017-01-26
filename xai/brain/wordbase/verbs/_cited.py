

from xai.brain.wordbase.verbs._cite import _CITE

#calss header
class _CITED(_CITE, ):
	def __init__(self,): 
		_CITE.__init__(self)
		self.name = "CITED"
		self.specie = 'verbs'
		self.basic = "cite"
		self.jsondata = {}
