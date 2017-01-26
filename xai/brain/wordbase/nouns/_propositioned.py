

from xai.brain.wordbase.nouns._proposition import _PROPOSITION

#calss header
class _PROPOSITIONED(_PROPOSITION, ):
	def __init__(self,): 
		_PROPOSITION.__init__(self)
		self.name = "PROPOSITIONED"
		self.specie = 'nouns'
		self.basic = "proposition"
		self.jsondata = {}
