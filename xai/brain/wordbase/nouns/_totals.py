

from xai.brain.wordbase.nouns._total import _TOTAL

#calss header
class _TOTALS(_TOTAL, ):
	def __init__(self,): 
		_TOTAL.__init__(self)
		self.name = "TOTALS"
		self.specie = 'nouns'
		self.basic = "total"
		self.jsondata = {}
