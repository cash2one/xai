

from xai.brain.wordbase.nouns._score import _SCORE

#calss header
class _SCORED(_SCORE, ):
	def __init__(self,): 
		_SCORE.__init__(self)
		self.name = "SCORED"
		self.specie = 'nouns'
		self.basic = "score"
		self.jsondata = {}
