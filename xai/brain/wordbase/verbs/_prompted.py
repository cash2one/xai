

from xai.brain.wordbase.verbs._prompt import _PROMPT

#calss header
class _PROMPTED(_PROMPT, ):
	def __init__(self,): 
		_PROMPT.__init__(self)
		self.name = "PROMPTED"
		self.specie = 'verbs'
		self.basic = "prompt"
		self.jsondata = {}
