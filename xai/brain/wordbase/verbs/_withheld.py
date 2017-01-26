

from xai.brain.wordbase.verbs._withhold import _WITHHOLD

#calss header
class _WITHHELD(_WITHHOLD, ):
	def __init__(self,): 
		_WITHHOLD.__init__(self)
		self.name = "WITHHELD"
		self.specie = 'verbs'
		self.basic = "withhold"
		self.jsondata = {}
