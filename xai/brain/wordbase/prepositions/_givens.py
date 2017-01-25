

from xai.brain.wordbase.prepositions._given import _GIVEN

#calss header
class _GIVENS(_GIVEN, ):
	def __init__(self,): 
		_GIVEN.__init__(self)
		self.name = "GIVENS"
		self.specie = 'prepositions'
		self.basic = "given"
		self.jsondata = {}
