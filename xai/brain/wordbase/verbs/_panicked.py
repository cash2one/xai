

from xai.brain.wordbase.verbs._panic import _PANIC

#calss header
class _PANICKED(_PANIC, ):
	def __init__(self,): 
		_PANIC.__init__(self)
		self.name = "PANICKED"
		self.specie = 'verbs'
		self.basic = "panic"
		self.jsondata = {}
