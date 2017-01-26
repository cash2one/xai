

from xai.brain.wordbase.nouns._author import _AUTHOR

#calss header
class _AUTHORS(_AUTHOR, ):
	def __init__(self,): 
		_AUTHOR.__init__(self)
		self.name = "AUTHORS"
		self.specie = 'nouns'
		self.basic = "author"
		self.jsondata = {}
