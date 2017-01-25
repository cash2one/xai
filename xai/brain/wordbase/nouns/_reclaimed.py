

from xai.brain.wordbase.nouns._reclaim import _RECLAIM

#calss header
class _RECLAIMED(_RECLAIM, ):
	def __init__(self,): 
		_RECLAIM.__init__(self)
		self.name = "RECLAIMED"
		self.specie = 'nouns'
		self.basic = "reclaim"
		self.jsondata = {}
