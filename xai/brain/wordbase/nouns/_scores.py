

from xai.brain.wordbase.nouns._score import _SCORE

#calss header
class _SCORES(_SCORE, ):
	def __init__(self,): 
		_SCORE.__init__(self)
		self.name = "SCORES"
		self.specie = 'nouns'
		self.basic = "score"
		self.jsondata = {}
