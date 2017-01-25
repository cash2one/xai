

from xai.brain.wordbase.verbs._blunt import _BLUNT

#calss header
class _BLUNTER(_BLUNT, ):
	def __init__(self,): 
		_BLUNT.__init__(self)
		self.name = "BLUNTER"
		self.specie = 'verbs'
		self.basic = "blunt"
		self.jsondata = {}
