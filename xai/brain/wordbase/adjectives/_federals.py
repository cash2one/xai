

from xai.brain.wordbase.adjectives._federal import _FEDERAL

#calss header
class _FEDERALS(_FEDERAL, ):
	def __init__(self,): 
		_FEDERAL.__init__(self)
		self.name = "FEDERALS"
		self.specie = 'adjectives'
		self.basic = "federal"
		self.jsondata = {}
