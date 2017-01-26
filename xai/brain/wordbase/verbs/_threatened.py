

from xai.brain.wordbase.verbs._threaten import _THREATEN

#calss header
class _THREATENED(_THREATEN, ):
	def __init__(self,): 
		_THREATEN.__init__(self)
		self.name = "THREATENED"
		self.specie = 'verbs'
		self.basic = "threaten"
		self.jsondata = {}
