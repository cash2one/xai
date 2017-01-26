

from xai.brain.wordbase.verbs._log import _LOG

#calss header
class _LOGS(_LOG, ):
	def __init__(self,): 
		_LOG.__init__(self)
		self.name = "LOGS"
		self.specie = 'verbs'
		self.basic = "log"
		self.jsondata = {}
