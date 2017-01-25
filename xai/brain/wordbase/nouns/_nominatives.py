

from xai.brain.wordbase.nouns._nominative import _NOMINATIVE

#calss header
class _NOMINATIVES(_NOMINATIVE, ):
	def __init__(self,): 
		_NOMINATIVE.__init__(self)
		self.name = "NOMINATIVES"
		self.specie = 'nouns'
		self.basic = "nominative"
		self.jsondata = {}
