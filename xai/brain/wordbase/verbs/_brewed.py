

from xai.brain.wordbase.verbs._brew import _BREW

#calss header
class _BREWED(_BREW, ):
	def __init__(self,): 
		_BREW.__init__(self)
		self.name = "BREWED"
		self.specie = 'verbs'
		self.basic = "brew"
		self.jsondata = {}
