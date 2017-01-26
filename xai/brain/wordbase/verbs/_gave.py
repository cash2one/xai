

from xai.brain.wordbase.verbs._give import _GIVE

#calss header
class _GAVE(_GIVE, ):
	def __init__(self,): 
		_GIVE.__init__(self)
		self.name = "GAVE"
		self.specie = 'verbs'
		self.basic = "give"
		self.jsondata = {}
