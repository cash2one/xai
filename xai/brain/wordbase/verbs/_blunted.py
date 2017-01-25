

from xai.brain.wordbase.verbs._blunt import _BLUNT

#calss header
class _BLUNTED(_BLUNT, ):
	def __init__(self,): 
		_BLUNT.__init__(self)
		self.name = "BLUNTED"
		self.specie = 'verbs'
		self.basic = "blunt"
		self.jsondata = {}
