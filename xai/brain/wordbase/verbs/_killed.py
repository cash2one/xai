

from xai.brain.wordbase.verbs._kill import _KILL

#calss header
class _KILLED(_KILL, ):
	def __init__(self,): 
		_KILL.__init__(self)
		self.name = "KILLED"
		self.specie = 'verbs'
		self.basic = "kill"
		self.jsondata = {}
