

from xai.brain.wordbase.verbs._decommission import _DECOMMISSION

#calss header
class _DECOMMISSIONED(_DECOMMISSION, ):
	def __init__(self,): 
		_DECOMMISSION.__init__(self)
		self.name = "DECOMMISSIONED"
		self.specie = 'verbs'
		self.basic = "decommission"
		self.jsondata = {}
