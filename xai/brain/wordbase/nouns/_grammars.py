

from xai.brain.wordbase.nouns._grammar import _GRAMMAR

#calss header
class _GRAMMARS(_GRAMMAR, ):
	def __init__(self,): 
		_GRAMMAR.__init__(self)
		self.name = "GRAMMARS"
		self.specie = 'nouns'
		self.basic = "grammar"
		self.jsondata = {}
