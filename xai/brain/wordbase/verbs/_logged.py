

from xai.brain.wordbase.verbs._log import _LOG

#calss header
class _LOGGED(_LOG, ):
	def __init__(self,): 
		_LOG.__init__(self)
		self.name = "LOGGED"
		self.specie = 'verbs'
		self.basic = "log"
		self.jsondata = {}
