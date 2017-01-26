

from xai.brain.wordbase.verbs._freight import _FREIGHT

#calss header
class _FREIGHTING(_FREIGHT, ):
	def __init__(self,): 
		_FREIGHT.__init__(self)
		self.name = "FREIGHTING"
		self.specie = 'verbs'
		self.basic = "freight"
		self.jsondata = {}
