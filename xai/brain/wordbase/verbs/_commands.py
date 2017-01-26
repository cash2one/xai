

from xai.brain.wordbase.verbs._command import _COMMAND

#calss header
class _COMMANDS(_COMMAND, ):
	def __init__(self,): 
		_COMMAND.__init__(self)
		self.name = "COMMANDS"
		self.specie = 'verbs'
		self.basic = "command"
		self.jsondata = {}
