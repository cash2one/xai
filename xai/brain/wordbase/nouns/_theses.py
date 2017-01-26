

from xai.brain.wordbase.nouns._thesis import _THESIS

#calss header
class _THESES(_THESIS, ):
	def __init__(self,): 
		_THESIS.__init__(self)
		self.name = "THESES"
		self.specie = 'nouns'
		self.basic = "thesis"
		self.jsondata = {}
