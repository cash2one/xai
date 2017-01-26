

from xai.brain.wordbase.verbs._diagnose import _DIAGNOSE

#calss header
class _DIAGNOSED(_DIAGNOSE, ):
	def __init__(self,): 
		_DIAGNOSE.__init__(self)
		self.name = "DIAGNOSED"
		self.specie = 'verbs'
		self.basic = "diagnose"
		self.jsondata = {}
