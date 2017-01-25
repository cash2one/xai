

from xai.brain.wordbase.verbs._reword import _REWORD

#calss header
class _REWORDS(_REWORD, ):
	def __init__(self,): 
		_REWORD.__init__(self)
		self.name = "REWORDS"
		self.specie = 'verbs'
		self.basic = "reword"
		self.jsondata = {}
