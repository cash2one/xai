

from xai.brain.wordbase.verbs._blacklist import _BLACKLIST

#calss header
class _BLACKLISTING(_BLACKLIST, ):
	def __init__(self,): 
		_BLACKLIST.__init__(self)
		self.name = "BLACKLISTING"
		self.specie = 'verbs'
		self.basic = "blacklist"
		self.jsondata = {}
