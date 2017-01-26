

from xai.brain.wordbase.nouns._tally import _TALLY

#calss header
class _TALLIES(_TALLY, ):
	def __init__(self,): 
		_TALLY.__init__(self)
		self.name = "TALLIES"
		self.specie = 'nouns'
		self.basic = "tally"
		self.jsondata = {}
