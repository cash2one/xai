

from xai.brain.wordbase.verbs._lock import _LOCK

#calss header
class _LOCKED(_LOCK, ):
	def __init__(self,): 
		_LOCK.__init__(self)
		self.name = "LOCKED"
		self.specie = 'verbs'
		self.basic = "lock"
		self.jsondata = {}
