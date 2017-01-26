

from xai.brain.wordbase.nouns._author import _AUTHOR

#calss header
class _AUTHORED(_AUTHOR, ):
	def __init__(self,): 
		_AUTHOR.__init__(self)
		self.name = "AUTHORED"
		self.specie = 'nouns'
		self.basic = "author"
		self.jsondata = {}
