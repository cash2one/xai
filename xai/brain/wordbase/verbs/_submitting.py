

from xai.brain.wordbase.verbs._submit import _SUBMIT

#calss header
class _SUBMITTING(_SUBMIT, ):
	def __init__(self,): 
		_SUBMIT.__init__(self)
		self.name = "SUBMITTING"
		self.specie = 'verbs'
		self.basic = "submit"
		self.jsondata = {}
