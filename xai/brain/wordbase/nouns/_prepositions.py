

from xai.brain.wordbase.nouns._preposition import _PREPOSITION

#calss header
class _PREPOSITIONS(_PREPOSITION, ):
	def __init__(self,): 
		_PREPOSITION.__init__(self)
		self.name = "PREPOSITIONS"
		self.specie = 'nouns'
		self.basic = "preposition"
		self.jsondata = {}
