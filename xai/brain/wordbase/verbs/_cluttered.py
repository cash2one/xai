

from xai.brain.wordbase.verbs._clutter import _CLUTTER

#calss header
class _CLUTTERED(_CLUTTER, ):
	def __init__(self,): 
		_CLUTTER.__init__(self)
		self.name = "CLUTTERED"
		self.specie = 'verbs'
		self.basic = "clutter"
		self.jsondata = {}
