

from xai.brain.wordbase.verbs._misapply import _MISAPPLY

#calss header
class _MISAPPLIED(_MISAPPLY, ):
	def __init__(self,): 
		_MISAPPLY.__init__(self)
		self.name = "MISAPPLIED"
		self.specie = 'verbs'
		self.basic = "misapply"
		self.jsondata = {}
