

from xai.brain.wordbase.verbs._yank import _YANK

#calss header
class _YANKED(_YANK, ):
	def __init__(self,): 
		_YANK.__init__(self)
		self.name = "YANKED"
		self.specie = 'verbs'
		self.basic = "yank"
		self.jsondata = {}
