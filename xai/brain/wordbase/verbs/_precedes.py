

from xai.brain.wordbase.verbs._precede import _PRECEDE

#calss header
class _PRECEDES(_PRECEDE, ):
	def __init__(self,): 
		_PRECEDE.__init__(self)
		self.name = "PRECEDES"
		self.specie = 'verbs'
		self.basic = "precede"
		self.jsondata = {}
