

from xai.brain.wordbase.nouns._command import _COMMAND

#calss header
class _COMMANDS(_COMMAND, ):
	def __init__(self,): 
		_COMMAND.__init__(self)
		self.name = "COMMANDS"
		self.specie = 'nouns'
		self.basic = "command"
		self.jsondata = {}
