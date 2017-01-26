

from xai.brain.wordbase.verbs._total import _TOTAL

#calss header
class _TOTALS(_TOTAL, ):
	def __init__(self,): 
		_TOTAL.__init__(self)
		self.name = "TOTALS"
		self.specie = 'verbs'
		self.basic = "total"
		self.jsondata = {}
