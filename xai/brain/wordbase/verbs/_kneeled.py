

from xai.brain.wordbase.verbs._kneel import _KNEEL

#calss header
class _KNEELED(_KNEEL, ):
	def __init__(self,): 
		_KNEEL.__init__(self)
		self.name = "KNEELED"
		self.specie = 'verbs'
		self.basic = "kneel"
		self.jsondata = {}
