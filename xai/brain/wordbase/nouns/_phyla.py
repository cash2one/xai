

from xai.brain.wordbase.nouns._phylum import _PHYLUM

#calss header
class _PHYLA(_PHYLUM, ):
	def __init__(self,): 
		_PHYLUM.__init__(self)
		self.name = "PHYLA"
		self.specie = 'nouns'
		self.basic = "phylum"
		self.jsondata = {}
