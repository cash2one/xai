

from xai.brain.wordbase.verbs._purge import _PURGE

#calss header
class _PURGED(_PURGE, ):
	def __init__(self,): 
		_PURGE.__init__(self)
		self.name = "PURGED"
		self.specie = 'verbs'
		self.basic = "purge"
		self.jsondata = {}
