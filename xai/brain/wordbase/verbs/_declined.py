

from xai.brain.wordbase.verbs._decline import _DECLINE

#calss header
class _DECLINED(_DECLINE, ):
	def __init__(self,): 
		_DECLINE.__init__(self)
		self.name = "DECLINED"
		self.specie = 'verbs'
		self.basic = "decline"
		self.jsondata = {}
