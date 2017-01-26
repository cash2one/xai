

from xai.brain.wordbase.verbs._silence import _SILENCE

#calss header
class _SILENCED(_SILENCE, ):
	def __init__(self,): 
		_SILENCE.__init__(self)
		self.name = "SILENCED"
		self.specie = 'verbs'
		self.basic = "silence"
		self.jsondata = {}
