

from xai.brain.wordbase.nouns._collocation import _COLLOCATION

#calss header
class _COLLOCATIONS(_COLLOCATION, ):
	def __init__(self,): 
		_COLLOCATION.__init__(self)
		self.name = "COLLOCATIONS"
		self.specie = 'nouns'
		self.basic = "collocation"
		self.jsondata = {}
