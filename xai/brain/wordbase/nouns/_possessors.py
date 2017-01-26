

from xai.brain.wordbase.nouns._possessor import _POSSESSOR

#calss header
class _POSSESSORS(_POSSESSOR, ):
	def __init__(self,): 
		_POSSESSOR.__init__(self)
		self.name = "POSSESSORS"
		self.specie = 'nouns'
		self.basic = "possessor"
		self.jsondata = {}
