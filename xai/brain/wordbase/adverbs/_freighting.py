

from xai.brain.wordbase.adverbs._freight import _FREIGHT

#calss header
class _FREIGHTING(_FREIGHT, ):
	def __init__(self,): 
		_FREIGHT.__init__(self)
		self.name = "FREIGHTING"
		self.specie = 'adverbs'
		self.basic = "freight"
		self.jsondata = {}
