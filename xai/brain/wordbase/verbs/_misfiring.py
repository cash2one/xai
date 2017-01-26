

from xai.brain.wordbase.verbs._misfire import _MISFIRE

#calss header
class _MISFIRING(_MISFIRE, ):
	def __init__(self,): 
		_MISFIRE.__init__(self)
		self.name = "MISFIRING"
		self.specie = 'verbs'
		self.basic = "misfire"
		self.jsondata = {}
