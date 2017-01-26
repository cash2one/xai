

from xai.brain.wordbase.verbs._hurt import _HURT

#calss header
class _HURTS(_HURT, ):
	def __init__(self,): 
		_HURT.__init__(self)
		self.name = "HURTS"
		self.specie = 'verbs'
		self.basic = "hurt"
		self.jsondata = {}
