

from xai.brain.wordbase.nouns._flair import _FLAIR

#calss header
class _FLAIRS(_FLAIR, ):
	def __init__(self,): 
		_FLAIR.__init__(self)
		self.name = "FLAIRS"
		self.specie = 'nouns'
		self.basic = "flair"
		self.jsondata = {}
