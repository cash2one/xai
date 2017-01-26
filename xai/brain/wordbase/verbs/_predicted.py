

from xai.brain.wordbase.verbs._predict import _PREDICT

#calss header
class _PREDICTED(_PREDICT, ):
	def __init__(self,): 
		_PREDICT.__init__(self)
		self.name = "PREDICTED"
		self.specie = 'verbs'
		self.basic = "predict"
		self.jsondata = {}
