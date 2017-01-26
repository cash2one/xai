

from xai.brain.wordbase.nouns._qualifier import _QUALIFIER

#calss header
class _QUALIFIERS(_QUALIFIER, ):
	def __init__(self,): 
		_QUALIFIER.__init__(self)
		self.name = "QUALIFIERS"
		self.specie = 'nouns'
		self.basic = "qualifier"
		self.jsondata = {}
