

from xai.brain.wordbase.verbs._silence import _SILENCE

#calss header
class _SILENCES(_SILENCE, ):
	def __init__(self,): 
		_SILENCE.__init__(self)
		self.name = "SILENCES"
		self.specie = 'verbs'
		self.basic = "silence"
		self.jsondata = {}
