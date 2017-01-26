

from xai.brain.wordbase.nouns._claim import _CLAIM

#calss header
class _CLAIMED(_CLAIM, ):
	def __init__(self,): 
		_CLAIM.__init__(self)
		self.name = "CLAIMED"
		self.specie = 'nouns'
		self.basic = "claim"
		self.jsondata = {}
