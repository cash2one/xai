

from xai.brain.wordbase.verbs._quarantine import _QUARANTINE

#calss header
class _QUARANTINED(_QUARANTINE, ):
	def __init__(self,): 
		_QUARANTINE.__init__(self)
		self.name = "QUARANTINED"
		self.specie = 'verbs'
		self.basic = "quarantine"
		self.jsondata = {}
