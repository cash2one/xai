

from xai.brain.wordbase.verbs._bluff import _BLUFF

#calss header
class _BLUFFED(_BLUFF, ):
	def __init__(self,): 
		_BLUFF.__init__(self)
		self.name = "BLUFFED"
		self.specie = 'verbs'
		self.basic = "bluff"
		self.jsondata = {}
