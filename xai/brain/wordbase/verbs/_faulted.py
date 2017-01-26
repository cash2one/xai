

from xai.brain.wordbase.verbs._fault import _FAULT

#calss header
class _FAULTED(_FAULT, ):
	def __init__(self,): 
		_FAULT.__init__(self)
		self.name = "FAULTED"
		self.specie = 'verbs'
		self.basic = "fault"
		self.jsondata = {}
