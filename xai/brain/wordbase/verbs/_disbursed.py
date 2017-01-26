

from xai.brain.wordbase.verbs._disburse import _DISBURSE

#calss header
class _DISBURSED(_DISBURSE, ):
	def __init__(self,): 
		_DISBURSE.__init__(self)
		self.name = "DISBURSED"
		self.specie = 'verbs'
		self.basic = "disburse"
		self.jsondata = {}
