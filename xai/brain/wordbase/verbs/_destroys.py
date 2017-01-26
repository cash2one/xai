

from xai.brain.wordbase.verbs._destroy import _DESTROY

#calss header
class _DESTROYS(_DESTROY, ):
	def __init__(self,): 
		_DESTROY.__init__(self)
		self.name = "DESTROYS"
		self.specie = 'verbs'
		self.basic = "destroy"
		self.jsondata = {}
