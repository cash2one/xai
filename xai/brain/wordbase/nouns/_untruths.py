

from xai.brain.wordbase.nouns._untruth import _UNTRUTH

#calss header
class _UNTRUTHS(_UNTRUTH, ):
	def __init__(self,): 
		_UNTRUTH.__init__(self)
		self.name = "UNTRUTHS"
		self.specie = 'nouns'
		self.basic = "untruth"
		self.jsondata = {}
