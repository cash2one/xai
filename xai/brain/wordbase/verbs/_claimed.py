

from xai.brain.wordbase.verbs._claim import _CLAIM

#calss header
class _CLAIMED(_CLAIM, ):
	def __init__(self,): 
		_CLAIM.__init__(self)
		self.name = "CLAIMED"
		self.specie = 'verbs'
		self.basic = "claim"
		self.jsondata = {}
