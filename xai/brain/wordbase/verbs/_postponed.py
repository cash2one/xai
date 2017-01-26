

from xai.brain.wordbase.verbs._postpone import _POSTPONE

#calss header
class _POSTPONED(_POSTPONE, ):
	def __init__(self,): 
		_POSTPONE.__init__(self)
		self.name = "POSTPONED"
		self.specie = 'verbs'
		self.basic = "postpone"
		self.jsondata = {}
