

from xai.brain.wordbase.verbs._patch import _PATCH

#calss header
class _PATCHING(_PATCH, ):
	def __init__(self,): 
		_PATCH.__init__(self)
		self.name = "PATCHING"
		self.specie = 'verbs'
		self.basic = "patch"
		self.jsondata = {}
