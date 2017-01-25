

from xai.brain.wordbase.verbs._patch import _PATCH

#calss header
class _PATCHED(_PATCH, ):
	def __init__(self,): 
		self.name = "PATCHED"
		self.basic = "patch"
		self.jsondata = {}
