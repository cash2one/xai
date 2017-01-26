

from xai.brain.wordbase.verbs._occlude import _OCCLUDE

#calss header
class _OCCLUDED(_OCCLUDE, ):
	def __init__(self,): 
		_OCCLUDE.__init__(self)
		self.name = "OCCLUDED"
		self.specie = 'verbs'
		self.basic = "occlude"
		self.jsondata = {}
