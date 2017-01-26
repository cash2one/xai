

from xai.brain.wordbase.verbs._chorus import _CHORUS

#calss header
class _CHORUSED(_CHORUS, ):
	def __init__(self,): 
		_CHORUS.__init__(self)
		self.name = "CHORUSED"
		self.specie = 'verbs'
		self.basic = "chorus"
		self.jsondata = {}
