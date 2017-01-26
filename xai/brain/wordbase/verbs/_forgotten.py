

from xai.brain.wordbase.verbs._forget import _FORGET

#calss header
class _FORGOTTEN(_FORGET, ):
	def __init__(self,): 
		_FORGET.__init__(self)
		self.name = "FORGOTTEN"
		self.specie = 'verbs'
		self.basic = "forget"
		self.jsondata = {}
