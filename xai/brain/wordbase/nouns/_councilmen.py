

from xai.brain.wordbase.nouns._councilman import _COUNCILMAN

#calss header
class _COUNCILMEN(_COUNCILMAN, ):
	def __init__(self,): 
		_COUNCILMAN.__init__(self)
		self.name = "COUNCILMEN"
		self.specie = 'nouns'
		self.basic = "councilman"
		self.jsondata = {}
