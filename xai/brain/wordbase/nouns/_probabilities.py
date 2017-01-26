

from xai.brain.wordbase.nouns._probability import _PROBABILITY

#calss header
class _PROBABILITIES(_PROBABILITY, ):
	def __init__(self,): 
		_PROBABILITY.__init__(self)
		self.name = "PROBABILITIES"
		self.specie = 'nouns'
		self.basic = "probability"
		self.jsondata = {}
