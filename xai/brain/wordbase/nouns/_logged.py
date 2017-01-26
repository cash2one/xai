

from xai.brain.wordbase.nouns._log import _LOG

#calss header
class _LOGGED(_LOG, ):
	def __init__(self,): 
		_LOG.__init__(self)
		self.name = "LOGGED"
		self.specie = 'nouns'
		self.basic = "log"
		self.jsondata = {}
