

from xai.brain.wordbase.verbs._miscount import _MISCOUNT

#calss header
class _MISCOUNTS(_MISCOUNT, ):
	def __init__(self,): 
		_MISCOUNT.__init__(self)
		self.name = "MISCOUNTS"
		self.specie = 'verbs'
		self.basic = "miscount"
		self.jsondata = {}
