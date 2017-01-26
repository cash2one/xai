

from xai.brain.wordbase.verbs._narrate import _NARRATE

#calss header
class _NARRATED(_NARRATE, ):
	def __init__(self,): 
		_NARRATE.__init__(self)
		self.name = "NARRATED"
		self.specie = 'verbs'
		self.basic = "narrate"
		self.jsondata = {}
