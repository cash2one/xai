

from xai.brain.wordbase.nouns._churn import _CHURN

#calss header
class _CHURNED(_CHURN, ):
	def __init__(self,): 
		_CHURN.__init__(self)
		self.name = "CHURNED"
		self.specie = 'nouns'
		self.basic = "churn"
		self.jsondata = {}
