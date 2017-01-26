

from xai.brain.wordbase.verbs._mispronounce import _MISPRONOUNCE

#calss header
class _MISPRONOUNCED(_MISPRONOUNCE, ):
	def __init__(self,): 
		_MISPRONOUNCE.__init__(self)
		self.name = "MISPRONOUNCED"
		self.specie = 'verbs'
		self.basic = "mispronounce"
		self.jsondata = {}
