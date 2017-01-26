

from xai.brain.wordbase.verbs._destroy import _DESTROY

#calss header
class _DESTROYED(_DESTROY, ):
	def __init__(self,): 
		_DESTROY.__init__(self)
		self.name = "DESTROYED"
		self.specie = 'verbs'
		self.basic = "destroy"
		self.jsondata = {}
