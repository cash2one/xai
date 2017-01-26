

from xai.brain.wordbase.verbs._submit import _SUBMIT

#calss header
class _SUBMITTED(_SUBMIT, ):
	def __init__(self,): 
		_SUBMIT.__init__(self)
		self.name = "SUBMITTED"
		self.specie = 'verbs'
		self.basic = "submit"
		self.jsondata = {}
