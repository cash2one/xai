

from xai.brain.wordbase.nouns._count import _COUNT

#calss header
class _COUNTS(_COUNT, ):
	def __init__(self,): 
		_COUNT.__init__(self)
		self.name = "COUNTS"
		self.specie = 'nouns'
		self.basic = "count"
		self.jsondata = {}
