

from xai.brain.wordbase.verbs._invoke import _INVOKE

#calss header
class _INVOKED(_INVOKE, ):
	def __init__(self,): 
		_INVOKE.__init__(self)
		self.name = "INVOKED"
		self.specie = 'verbs'
		self.basic = "invoke"
		self.jsondata = {}
