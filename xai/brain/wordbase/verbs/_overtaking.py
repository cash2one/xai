

from xai.brain.wordbase.verbs._overtake import _OVERTAKE

#calss header
class _OVERTAKING(_OVERTAKE, ):
	def __init__(self,): 
		_OVERTAKE.__init__(self)
		self.name = "OVERTAKING"
		self.specie = 'verbs'
		self.basic = "overtake"
		self.jsondata = {}
