

from xai.brain.wordbase.nouns._strength import _STRENGTH

#calss header
class _STRENGTHS(_STRENGTH, ):
	def __init__(self,): 
		_STRENGTH.__init__(self)
		self.name = "STRENGTHS"
		self.specie = 'nouns'
		self.basic = "strength"
		self.jsondata = {}
