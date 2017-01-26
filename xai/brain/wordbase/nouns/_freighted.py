

from xai.brain.wordbase.nouns._freight import _FREIGHT

#calss header
class _FREIGHTED(_FREIGHT, ):
	def __init__(self,): 
		_FREIGHT.__init__(self)
		self.name = "FREIGHTED"
		self.specie = 'nouns'
		self.basic = "freight"
		self.jsondata = {}
