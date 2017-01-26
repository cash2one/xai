

from xai.brain.wordbase.nouns._answer import _ANSWER

#calss header
class _ANSWERED(_ANSWER, ):
	def __init__(self,): 
		_ANSWER.__init__(self)
		self.name = "ANSWERED"
		self.specie = 'nouns'
		self.basic = "answer"
		self.jsondata = {}
