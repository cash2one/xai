

from xai.brain.wordbase.verbs._probe import _PROBE

#calss header
class _PROBED(_PROBE, ):
	def __init__(self,): 
		_PROBE.__init__(self)
		self.name = "PROBED"
		self.specie = 'verbs'
		self.basic = "probe"
		self.jsondata = {}
