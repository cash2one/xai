

from xai.brain.wordbase.nouns._chorus import _CHORUS

#calss header
class _CHORUSED(_CHORUS, ):
	def __init__(self,): 
		_CHORUS.__init__(self)
		self.name = "CHORUSED"
		self.specie = 'nouns'
		self.basic = "chorus"
		self.jsondata = {}
