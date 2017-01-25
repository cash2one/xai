

from xai.brain.wordbase.nouns._veto import _VETO

#calss header
class _VETOED(_VETO, ):
	def __init__(self,): 
		_VETO.__init__(self)
		self.name = "VETOED"
		self.specie = 'nouns'
		self.basic = "veto"
		self.jsondata = {}
