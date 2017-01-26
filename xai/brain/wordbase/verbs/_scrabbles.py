

from xai.brain.wordbase.verbs._scrabble import _SCRABBLE

#calss header
class _SCRABBLES(_SCRABBLE, ):
	def __init__(self,): 
		_SCRABBLE.__init__(self)
		self.name = "SCRABBLES"
		self.specie = 'verbs'
		self.basic = "scrabble"
		self.jsondata = {}
