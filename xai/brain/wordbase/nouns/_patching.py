

from xai.brain.wordbase.nouns._patch import _PATCH

#calss header
class _PATCHING(_PATCH, ):
	def __init__(self,): 
		_PATCH.__init__(self)
		self.name = "PATCHING"
		self.specie = 'nouns'
		self.basic = "patch"
		self.jsondata = {}
