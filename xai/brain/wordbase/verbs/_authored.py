

from xai.brain.wordbase.verbs._author import _AUTHOR

#calss header
class _AUTHORED(_AUTHOR, ):
	def __init__(self,): 
		_AUTHOR.__init__(self)
		self.name = "AUTHORED"
		self.specie = 'verbs'
		self.basic = "author"
		self.jsondata = {}
