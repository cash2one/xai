

from xai.brain.wordbase.nouns._rank import _RANK

#calss header
class _RANKED(_RANK, ):
	def __init__(self,): 
		_RANK.__init__(self)
		self.name = "RANKED"
		self.specie = 'nouns'
		self.basic = "rank"
		self.jsondata = {}
