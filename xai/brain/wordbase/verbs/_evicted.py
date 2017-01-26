

from xai.brain.wordbase.verbs._evict import _EVICT

#calss header
class _EVICTED(_EVICT, ):
	def __init__(self,): 
		_EVICT.__init__(self)
		self.name = "EVICTED"
		self.specie = 'verbs'
		self.basic = "evict"
		self.jsondata = {}
