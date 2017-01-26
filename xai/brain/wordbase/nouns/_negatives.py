

from xai.brain.wordbase.nouns._negative import _NEGATIVE

#calss header
class _NEGATIVES(_NEGATIVE, ):
	def __init__(self,): 
		_NEGATIVE.__init__(self)
		self.name = "NEGATIVES"
		self.specie = 'nouns'
		self.basic = "negative"
		self.jsondata = {}
