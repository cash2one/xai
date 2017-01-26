

from xai.brain.wordbase.verbs._submit import _SUBMIT

#calss header
class _SUBMITS(_SUBMIT, ):
	def __init__(self,): 
		_SUBMIT.__init__(self)
		self.name = "SUBMITS"
		self.specie = 'verbs'
		self.basic = "submit"
		self.jsondata = {}
