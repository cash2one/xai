

from xai.brain.wordbase.verbs._kneel import _KNEEL

#calss header
class _KNEELING(_KNEEL, ):
	def __init__(self,): 
		_KNEEL.__init__(self)
		self.name = "KNEELING"
		self.specie = 'verbs'
		self.basic = "kneel"
		self.jsondata = {}
