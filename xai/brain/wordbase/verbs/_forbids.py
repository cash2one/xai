

from xai.brain.wordbase.verbs._forbid import _FORBID

#calss header
class _FORBIDS(_FORBID, ):
	def __init__(self,): 
		_FORBID.__init__(self)
		self.name = "FORBIDS"
		self.specie = 'verbs'
		self.basic = "forbid"
		self.jsondata = {}
