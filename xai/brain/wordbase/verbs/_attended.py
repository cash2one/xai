

from xai.brain.wordbase.verbs._attend import _ATTEND

#calss header
class _ATTENDED(_ATTEND, ):
	def __init__(self,): 
		_ATTEND.__init__(self)
		self.name = "ATTENDED"
		self.specie = 'verbs'
		self.basic = "attend"
		self.jsondata = {}
