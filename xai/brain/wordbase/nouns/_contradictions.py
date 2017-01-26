

from xai.brain.wordbase.nouns._contradiction import _CONTRADICTION

#calss header
class _CONTRADICTIONS(_CONTRADICTION, ):
	def __init__(self,): 
		_CONTRADICTION.__init__(self)
		self.name = "CONTRADICTIONS"
		self.specie = 'nouns'
		self.basic = "contradiction"
		self.jsondata = {}
