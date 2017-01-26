

from xai.brain.wordbase.nouns._tally import _TALLY

#calss header
class _TALLIED(_TALLY, ):
	def __init__(self,): 
		_TALLY.__init__(self)
		self.name = "TALLIED"
		self.specie = 'nouns'
		self.basic = "tally"
		self.jsondata = {}
