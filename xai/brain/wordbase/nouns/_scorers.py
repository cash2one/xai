

from xai.brain.wordbase.nouns._scorer import _SCORER

#calss header
class _SCORERS(_SCORER, ):
	def __init__(self,): 
		_SCORER.__init__(self)
		self.name = "SCORERS"
		self.specie = 'nouns'
		self.basic = "scorer"
		self.jsondata = {}
