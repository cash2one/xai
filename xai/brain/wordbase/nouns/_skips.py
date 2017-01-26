

from xai.brain.wordbase.nouns._skip import _SKIP

#calss header
class _SKIPS(_SKIP, ):
	def __init__(self,): 
		_SKIP.__init__(self)
		self.name = "SKIPS"
		self.specie = 'nouns'
		self.basic = "skip"
		self.jsondata = {}
