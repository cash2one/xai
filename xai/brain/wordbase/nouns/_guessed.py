

from xai.brain.wordbase.nouns._guess import _GUESS

#calss header
class _GUESSED(_GUESS, ):
	def __init__(self,): 
		_GUESS.__init__(self)
		self.name = "GUESSED"
		self.specie = 'nouns'
		self.basic = "guess"
		self.jsondata = {}
