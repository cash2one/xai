

from xai.brain.wordbase.verbs._fluff import _FLUFF

#calss header
class _FLUFFED(_FLUFF, ):
	def __init__(self,): 
		_FLUFF.__init__(self)
		self.name = "FLUFFED"
		self.specie = 'verbs'
		self.basic = "fluff"
		self.jsondata = {}
