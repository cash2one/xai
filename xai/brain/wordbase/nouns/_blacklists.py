

from xai.brain.wordbase.nouns._blacklist import _BLACKLIST

#calss header
class _BLACKLISTS(_BLACKLIST, ):
	def __init__(self,): 
		_BLACKLIST.__init__(self)
		self.name = "BLACKLISTS"
		self.specie = 'nouns'
		self.basic = "blacklist"
		self.jsondata = {}
