

from xai.brain.wordbase.adverbs._freight import _FREIGHT

#calss header
class _FREIGHTS(_FREIGHT, ):
	def __init__(self,): 
		_FREIGHT.__init__(self)
		self.name = "FREIGHTS"
		self.specie = 'adverbs'
		self.basic = "freight"
		self.jsondata = {}
