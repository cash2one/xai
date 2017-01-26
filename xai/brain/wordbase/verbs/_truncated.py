

from xai.brain.wordbase.verbs._truncate import _TRUNCATE

#calss header
class _TRUNCATED(_TRUNCATE, ):
	def __init__(self,): 
		_TRUNCATE.__init__(self)
		self.name = "TRUNCATED"
		self.specie = 'verbs'
		self.basic = "truncate"
		self.jsondata = {}
