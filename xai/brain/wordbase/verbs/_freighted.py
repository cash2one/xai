

from xai.brain.wordbase.verbs._freight import _FREIGHT

#calss header
class _FREIGHTED(_FREIGHT, ):
	def __init__(self,): 
		_FREIGHT.__init__(self)
		self.name = "FREIGHTED"
		self.specie = 'verbs'
		self.basic = "freight"
		self.jsondata = {}
