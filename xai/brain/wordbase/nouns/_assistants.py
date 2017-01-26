

from xai.brain.wordbase.nouns._assistant import _ASSISTANT

#calss header
class _ASSISTANTS(_ASSISTANT, ):
	def __init__(self,): 
		_ASSISTANT.__init__(self)
		self.name = "ASSISTANTS"
		self.specie = 'nouns'
		self.basic = "assistant"
		self.jsondata = {}
