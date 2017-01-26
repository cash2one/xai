

from xai.brain.wordbase.verbs._execute import _EXECUTE

#calss header
class _EXECUTED(_EXECUTE, ):
	def __init__(self,): 
		_EXECUTE.__init__(self)
		self.name = "EXECUTED"
		self.specie = 'verbs'
		self.basic = "execute"
		self.jsondata = {}
