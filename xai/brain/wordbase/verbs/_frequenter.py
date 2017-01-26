

from xai.brain.wordbase.verbs._frequent import _FREQUENT

#calss header
class _FREQUENTER(_FREQUENT, ):
	def __init__(self,): 
		_FREQUENT.__init__(self)
		self.name = "FREQUENTER"
		self.specie = 'verbs'
		self.basic = "frequent"
		self.jsondata = {}
