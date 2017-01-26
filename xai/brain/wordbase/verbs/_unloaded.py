

from xai.brain.wordbase.verbs._unload import _UNLOAD

#calss header
class _UNLOADED(_UNLOAD, ):
	def __init__(self,): 
		_UNLOAD.__init__(self)
		self.name = "UNLOADED"
		self.specie = 'verbs'
		self.basic = "unload"
		self.jsondata = {}
