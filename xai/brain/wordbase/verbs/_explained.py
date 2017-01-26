

from xai.brain.wordbase.verbs._explain import _EXPLAIN

#calss header
class _EXPLAINED(_EXPLAIN, ):
	def __init__(self,): 
		_EXPLAIN.__init__(self)
		self.name = "EXPLAINED"
		self.specie = 'verbs'
		self.basic = "explain"
		self.jsondata = {}
