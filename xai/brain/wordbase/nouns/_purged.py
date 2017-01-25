

from xai.brain.wordbase.nouns._purge import _PURGE

#calss header
class _PURGED(_PURGE, ):
	def __init__(self,): 
		_PURGE.__init__(self)
		self.name = "PURGED"
		self.specie = 'nouns'
		self.basic = "purge"
		self.jsondata = {}
