

from xai.brain.wordbase.verbs._rewrite import _REWRITE

#calss header
class _REWRITES(_REWRITE, ):
	def __init__(self,): 
		_REWRITE.__init__(self)
		self.name = "REWRITES"
		self.specie = 'verbs'
		self.basic = "rewrite"
		self.jsondata = {}
