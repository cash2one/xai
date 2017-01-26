

from xai.brain.wordbase.nouns._facet import _FACET

#calss header
class _FACETS(_FACET, ):
	def __init__(self,): 
		_FACET.__init__(self)
		self.name = "FACETS"
		self.specie = 'nouns'
		self.basic = "facet"
		self.jsondata = {}
