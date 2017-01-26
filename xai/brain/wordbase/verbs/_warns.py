

from xai.brain.wordbase.verbs._warn import _WARN

#calss header
class _WARNS(_WARN, ):
	def __init__(self,): 
		_WARN.__init__(self)
		self.name = "WARNS"
		self.specie = 'verbs'
		self.basic = "warn"
		self.jsondata = {}
