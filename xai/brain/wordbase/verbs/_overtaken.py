

from xai.brain.wordbase.verbs._overtake import _OVERTAKE

#calss header
class _OVERTAKEN(_OVERTAKE, ):
	def __init__(self,): 
		_OVERTAKE.__init__(self)
		self.name = "OVERTAKEN"
		self.specie = 'verbs'
		self.basic = "overtake"
		self.jsondata = {}
