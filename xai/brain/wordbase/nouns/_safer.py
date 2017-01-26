

from xai.brain.wordbase.nouns._safe import _SAFE

#calss header
class _SAFER(_SAFE, ):
	def __init__(self,): 
		_SAFE.__init__(self)
		self.name = "SAFER"
		self.specie = 'nouns'
		self.basic = "safe"
		self.jsondata = {}
