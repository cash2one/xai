

from xai.brain.wordbase.nouns._search import _SEARCH

#calss header
class _SEARCHED(_SEARCH, ):
	def __init__(self,): 
		_SEARCH.__init__(self)
		self.name = "SEARCHED"
		self.specie = 'nouns'
		self.basic = "search"
		self.jsondata = {}
