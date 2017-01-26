

from xai.brain.wordbase.nouns._bias import _BIAS

#calss header
class _BIASSED(_BIAS, ):
	def __init__(self,): 
		_BIAS.__init__(self)
		self.name = "BIASSED"
		self.specie = 'nouns'
		self.basic = "bias"
		self.jsondata = {}
