

from xai.brain.wordbase.nouns._negative import _NEGATIVE

#calss header
class _NEGATIVED(_NEGATIVE, ):
	def __init__(self,): 
		_NEGATIVE.__init__(self)
		self.name = "NEGATIVED"
		self.specie = 'nouns'
		self.basic = "negative"
		self.jsondata = {}
