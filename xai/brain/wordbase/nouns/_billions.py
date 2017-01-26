

from xai.brain.wordbase.nouns._billion import _BILLION

#calss header
class _BILLIONS(_BILLION, ):
	def __init__(self,): 
		_BILLION.__init__(self)
		self.name = "BILLIONS"
		self.specie = 'nouns'
		self.basic = "billion"
		self.jsondata = {}
