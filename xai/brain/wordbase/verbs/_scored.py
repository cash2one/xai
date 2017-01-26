

from xai.brain.wordbase.verbs._score import _SCORE

#calss header
class _SCORED(_SCORE, ):
	def __init__(self,): 
		_SCORE.__init__(self)
		self.name = "SCORED"
		self.specie = 'verbs'
		self.basic = "score"
		self.jsondata = {}
