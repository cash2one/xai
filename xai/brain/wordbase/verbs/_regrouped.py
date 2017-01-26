

from xai.brain.wordbase.verbs._regroup import _REGROUP

#calss header
class _REGROUPED(_REGROUP, ):
	def __init__(self,): 
		_REGROUP.__init__(self)
		self.name = "REGROUPED"
		self.specie = 'verbs'
		self.basic = "regroup"
		self.jsondata = {}
