

from xai.brain.wordbase.verbs._sleep import _SLEEP

#calss header
class _SLEEPING(_SLEEP, ):
	def __init__(self,): 
		_SLEEP.__init__(self)
		self.name = "SLEEPING"
		self.specie = 'verbs'
		self.basic = "sleep"
		self.jsondata = {}
