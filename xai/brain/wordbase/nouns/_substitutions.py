

from xai.brain.wordbase.nouns._substitution import _SUBSTITUTION

#calss header
class _SUBSTITUTIONS(_SUBSTITUTION, ):
	def __init__(self,): 
		_SUBSTITUTION.__init__(self)
		self.name = "SUBSTITUTIONS"
		self.specie = 'nouns'
		self.basic = "substitution"
		self.jsondata = {}
