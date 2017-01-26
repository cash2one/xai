

from xai.brain.wordbase.verbs._predict import _PREDICT

#calss header
class _PREDICTS(_PREDICT, ):
	def __init__(self,): 
		_PREDICT.__init__(self)
		self.name = "PREDICTS"
		self.specie = 'verbs'
		self.basic = "predict"
		self.jsondata = {}
