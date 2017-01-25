

from xai.brain.wordbase.verbs._reclaim import _RECLAIM

#calss header
class _RECLAIMED(_RECLAIM, ):
	def __init__(self,): 
		_RECLAIM.__init__(self)
		self.name = "RECLAIMED"
		self.specie = 'verbs'
		self.basic = "reclaim"
		self.jsondata = {}
