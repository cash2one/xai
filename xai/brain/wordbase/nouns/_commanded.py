

from xai.brain.wordbase.nouns._command import _COMMAND

#calss header
class _COMMANDED(_COMMAND, ):
	def __init__(self,): 
		_COMMAND.__init__(self)
		self.name = "COMMANDED"
		self.specie = 'nouns'
		self.basic = "command"
		self.jsondata = {}
