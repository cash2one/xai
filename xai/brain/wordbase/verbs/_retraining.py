

from xai.brain.wordbase.verbs._retrain import _RETRAIN

#calss header
class _RETRAINING(_RETRAIN, ):
	def __init__(self,): 
		_RETRAIN.__init__(self)
		self.name = "RETRAINING"
		self.specie = 'verbs'
		self.basic = "retrain"
		self.jsondata = {}
