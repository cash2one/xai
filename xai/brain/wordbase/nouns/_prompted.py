

from xai.brain.wordbase.nouns._prompt import _PROMPT

#calss header
class _PROMPTED(_PROMPT, ):
	def __init__(self,): 
		_PROMPT.__init__(self)
		self.name = "PROMPTED"
		self.specie = 'nouns'
		self.basic = "prompt"
		self.jsondata = {}
