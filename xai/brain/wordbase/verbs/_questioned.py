

from xai.brain.wordbase.verbs._question import _QUESTION

#calss header
class _QUESTIONED(_QUESTION, ):
	def __init__(self,): 
		_QUESTION.__init__(self)
		self.name = "QUESTIONED"
		self.specie = 'verbs'
		self.basic = "question"
		self.jsondata = {}
