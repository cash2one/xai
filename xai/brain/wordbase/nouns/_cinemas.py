

from xai.brain.wordbase.nouns._cinema import _CINEMA

#calss header
class _CINEMAS(_CINEMA, ):
	def __init__(self,): 
		_CINEMA.__init__(self)
		self.name = "CINEMAS"
		self.specie = 'nouns'
		self.basic = "cinema"
		self.jsondata = {}
