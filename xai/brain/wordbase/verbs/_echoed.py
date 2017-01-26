

from xai.brain.wordbase.verbs._echo import _ECHO

#calss header
class _ECHOED(_ECHO, ):
	def __init__(self,): 
		_ECHO.__init__(self)
		self.name = "ECHOED"
		self.specie = 'verbs'
		self.basic = "echo"
		self.jsondata = {}
