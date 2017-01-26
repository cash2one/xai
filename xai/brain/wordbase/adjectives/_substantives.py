

from xai.brain.wordbase.adjectives._substantive import _SUBSTANTIVE

#calss header
class _SUBSTANTIVES(_SUBSTANTIVE, ):
	def __init__(self,): 
		_SUBSTANTIVE.__init__(self)
		self.name = "SUBSTANTIVES"
		self.specie = 'adjectives'
		self.basic = "substantive"
		self.jsondata = {}
