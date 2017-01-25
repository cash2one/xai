

from xai.brain.wordbase.nouns._lock import _LOCK

#calss header
class _LOCKED(_LOCK, ):
	def __init__(self,): 
		_LOCK.__init__(self)
		self.name = "LOCKED"
		self.specie = 'nouns'
		self.basic = "lock"
		self.jsondata = {}
