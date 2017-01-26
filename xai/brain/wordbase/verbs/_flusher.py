

from xai.brain.wordbase.verbs._flush import _FLUSH

#calss header
class _FLUSHER(_FLUSH, ):
	def __init__(self,): 
		_FLUSH.__init__(self)
		self.name = "FLUSHER"
		self.specie = 'verbs'
		self.basic = "flush"
		self.jsondata = {}
