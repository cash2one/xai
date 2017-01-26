

from xai.brain.wordbase.nouns._count import _COUNT

#calss header
class _COUNTED(_COUNT, ):
	def __init__(self,): 
		_COUNT.__init__(self)
		self.name = "COUNTED"
		self.specie = 'nouns'
		self.basic = "count"
		self.jsondata = {}
