

from xai.brain.wordbase.verbs._reactivate import _REACTIVATE

#calss header
class _REACTIVATED(_REACTIVATE, ):
	def __init__(self,): 
		_REACTIVATE.__init__(self)
		self.name = "REACTIVATED"
		self.specie = 'verbs'
		self.basic = "reactivate"
		self.jsondata = {}
