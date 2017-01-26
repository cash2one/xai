

from xai.brain.wordbase.verbs._reword import _REWORD

#calss header
class _REWORDED(_REWORD, ):
	def __init__(self,): 
		_REWORD.__init__(self)
		self.name = "REWORDED"
		self.specie = 'verbs'
		self.basic = "reword"
		self.jsondata = {}
