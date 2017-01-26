

from xai.brain.wordbase.adjectives._negative import _NEGATIVE

#calss header
class _NEGATIVES(_NEGATIVE, ):
	def __init__(self,): 
		_NEGATIVE.__init__(self)
		self.name = "NEGATIVES"
		self.specie = 'adjectives'
		self.basic = "negative"
		self.jsondata = {}
