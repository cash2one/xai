

from xai.brain.wordbase.verbs._donate import _DONATE

#calss header
class _DONATED(_DONATE, ):
	def __init__(self,): 
		_DONATE.__init__(self)
		self.name = "DONATED"
		self.specie = 'verbs'
		self.basic = "donate"
		self.jsondata = {}
