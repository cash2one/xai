

from xai.brain.wordbase.verbs._requisition import _REQUISITION

#calss header
class _REQUISITIONS(_REQUISITION, ):
	def __init__(self,): 
		_REQUISITION.__init__(self)
		self.name = "REQUISITIONS"
		self.specie = 'verbs'
		self.basic = "requisition"
		self.jsondata = {}
