

from xai.brain.wordbase.verbs._adjourn import _ADJOURN

#calss header
class _ADJOURNED(_ADJOURN, ):
	def __init__(self,): 
		_ADJOURN.__init__(self)
		self.name = "ADJOURNED"
		self.specie = 'verbs'
		self.basic = "adjourn"
		self.jsondata = {}
