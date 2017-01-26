

from xai.brain.wordbase.verbs._tell import _TELL

#calss header
class _TOLD(_TELL, ):
	def __init__(self,): 
		_TELL.__init__(self)
		self.name = "TOLD"
		self.specie = 'verbs'
		self.basic = "tell"
		self.jsondata = {}
