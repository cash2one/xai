

from xai.brain.wordbase.nouns._telex import _TELEX

#calss header
class _TELEXED(_TELEX, ):
	def __init__(self,): 
		_TELEX.__init__(self)
		self.name = "TELEXED"
		self.specie = 'nouns'
		self.basic = "telex"
		self.jsondata = {}
