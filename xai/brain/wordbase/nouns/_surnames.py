

from xai.brain.wordbase.nouns._surname import _SURNAME

#calss header
class _SURNAMES(_SURNAME, ):
	def __init__(self,): 
		_SURNAME.__init__(self)
		self.name = "SURNAMES"
		self.specie = 'nouns'
		self.basic = "surname"
		self.jsondata = {}
