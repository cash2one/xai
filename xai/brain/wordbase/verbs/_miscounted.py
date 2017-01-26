

from xai.brain.wordbase.verbs._miscount import _MISCOUNT

#calss header
class _MISCOUNTED(_MISCOUNT, ):
	def __init__(self,): 
		_MISCOUNT.__init__(self)
		self.name = "MISCOUNTED"
		self.specie = 'verbs'
		self.basic = "miscount"
		self.jsondata = {}
