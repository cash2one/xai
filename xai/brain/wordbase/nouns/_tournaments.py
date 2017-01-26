

from xai.brain.wordbase.nouns._tournament import _TOURNAMENT

#calss header
class _TOURNAMENTS(_TOURNAMENT, ):
	def __init__(self,): 
		_TOURNAMENT.__init__(self)
		self.name = "TOURNAMENTS"
		self.specie = 'nouns'
		self.basic = "tournament"
		self.jsondata = {}
