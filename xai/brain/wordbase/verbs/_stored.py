

from xai.brain.wordbase.verbs._store import _STORE

#calss header
class _STORED(_STORE, ):
	def __init__(self,): 
		_STORE.__init__(self)
		self.name = "STORED"
		self.specie = 'verbs'
		self.basic = "store"
		self.jsondata = {}
