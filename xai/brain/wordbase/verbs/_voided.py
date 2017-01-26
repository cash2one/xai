

from xai.brain.wordbase.verbs._void import _VOID

#calss header
class _VOIDED(_VOID, ):
	def __init__(self,): 
		_VOID.__init__(self)
		self.name = "VOIDED"
		self.specie = 'verbs'
		self.basic = "void"
		self.jsondata = {}
