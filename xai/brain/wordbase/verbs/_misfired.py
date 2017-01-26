

from xai.brain.wordbase.verbs._misfire import _MISFIRE

#calss header
class _MISFIRED(_MISFIRE, ):
	def __init__(self,): 
		_MISFIRE.__init__(self)
		self.name = "MISFIRED"
		self.specie = 'verbs'
		self.basic = "misfire"
		self.jsondata = {}
