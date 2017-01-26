

from xai.brain.wordbase.nouns._question import _QUESTION

#calss header
class _QUESTIONED(_QUESTION, ):
	def __init__(self,): 
		_QUESTION.__init__(self)
		self.name = "QUESTIONED"
		self.specie = 'nouns'
		self.basic = "question"
		self.jsondata = {}
