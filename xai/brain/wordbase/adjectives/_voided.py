

from xai.brain.wordbase.adjectives._void import _VOID

#calss header
class _VOIDED(_VOID, ):
	def __init__(self,): 
		_VOID.__init__(self)
		self.name = "VOIDED"
		self.specie = 'adjectives'
		self.basic = "void"
		self.jsondata = {}
