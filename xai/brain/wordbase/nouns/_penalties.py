

from xai.brain.wordbase.nouns._penalty import _PENALTY

#calss header
class _PENALTIES(_PENALTY, ):
	def __init__(self,): 
		_PENALTY.__init__(self)
		self.name = "PENALTIES"
		self.specie = 'nouns'
		self.basic = "penalty"
		self.jsondata = {}
