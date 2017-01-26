

from xai.brain.wordbase.verbs._exit import _EXIT

#calss header
class _EXITING(_EXIT, ):
	def __init__(self,): 
		_EXIT.__init__(self)
		self.name = "EXITING"
		self.specie = 'verbs'
		self.basic = "exit"
		self.jsondata = {}
