

from xai.brain.wordbase.verbs._exit import _EXIT

#calss header
class _EXITED(_EXIT, ):
	def __init__(self,): 
		_EXIT.__init__(self)
		self.name = "EXITED"
		self.specie = 'verbs'
		self.basic = "exit"
		self.jsondata = {}
