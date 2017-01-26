

from xai.brain.wordbase.nouns._hedge import _HEDGE

#calss header
class _HEDGED(_HEDGE, ):
	def __init__(self,): 
		_HEDGE.__init__(self)
		self.name = "HEDGED"
		self.specie = 'nouns'
		self.basic = "hedge"
		self.jsondata = {}
