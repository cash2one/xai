

from xai.brain.wordbase.verbs._churn import _CHURN

#calss header
class _CHURNED(_CHURN, ):
	def __init__(self,): 
		_CHURN.__init__(self)
		self.name = "CHURNED"
		self.specie = 'verbs'
		self.basic = "churn"
		self.jsondata = {}
