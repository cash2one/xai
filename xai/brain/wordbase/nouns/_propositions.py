

from xai.brain.wordbase.nouns._proposition import _PROPOSITION

#calss header
class _PROPOSITIONS(_PROPOSITION, ):
	def __init__(self,): 
		_PROPOSITION.__init__(self)
		self.name = "PROPOSITIONS"
		self.specie = 'nouns'
		self.basic = "proposition"
		self.jsondata = {}
