

from xai.brain.wordbase.verbs._cancel import _CANCEL

#calss header
class _CANCELLED(_CANCEL, ):
	def __init__(self,): 
		_CANCEL.__init__(self)
		self.name = "CANCELLED"
		self.specie = 'verbs'
		self.basic = "cancel"
		self.jsondata = {}
