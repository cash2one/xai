

from xai.brain.wordbase.nouns._prediction import _PREDICTION

#calss header
class _PREDICTIONS(_PREDICTION, ):
	def __init__(self,): 
		_PREDICTION.__init__(self)
		self.name = "PREDICTIONS"
		self.specie = 'nouns'
		self.basic = "prediction"
		self.jsondata = {}
