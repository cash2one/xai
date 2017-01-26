

from xai.brain.wordbase.verbs._silence import _SILENCE

#calss header
class _SILENCING(_SILENCE, ):
	def __init__(self,): 
		_SILENCE.__init__(self)
		self.name = "SILENCING"
		self.specie = 'verbs'
		self.basic = "silence"
		self.jsondata = {}
