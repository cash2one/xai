

from xai.brain.wordbase.verbs._give import _GIVE

#calss header
class _GIVES(_GIVE, ):
	def __init__(self,): 
		_GIVE.__init__(self)
		self.name = "GIVES"
		self.specie = 'verbs'
		self.basic = "give"
		self.jsondata = {}
