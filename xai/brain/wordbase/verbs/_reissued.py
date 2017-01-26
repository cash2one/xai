

from xai.brain.wordbase.verbs._reissue import _REISSUE

#calss header
class _REISSUED(_REISSUE, ):
	def __init__(self,): 
		_REISSUE.__init__(self)
		self.name = "REISSUED"
		self.specie = 'verbs'
		self.basic = "reissue"
		self.jsondata = {}
