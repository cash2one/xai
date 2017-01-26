

from xai.brain.wordbase.nouns._quarantine import _QUARANTINE

#calss header
class _QUARANTINED(_QUARANTINE, ):
	def __init__(self,): 
		_QUARANTINE.__init__(self)
		self.name = "QUARANTINED"
		self.specie = 'nouns'
		self.basic = "quarantine"
		self.jsondata = {}
